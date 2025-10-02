#!/usr/bin/env python3
"""
tag_papers.py — Adds specific sub-topic tags to each paper in
filter_papers.json.

This script takes papers already classified as "AI for Hardware/System" and
assigns one to three granular tags (e.g., 'Verification', 'Synthesis') to each.

Usage Example
-------------
# Tag all un-tagged papers using the default model gpt-4o
python tag_papers.py --input _data/filter_papers.json \
                     --output _data/tagged_papers.json

Optional Arguments
------------------
--input FILE       Input JSON (default: _data/filter_papers.json)
--output FILE      Output JSON (default: _data/tagged_papers.json)
--model MODEL      OpenAI model name (default: gpt-4o, can be changed to gpt-3.5-turbo, etc.)
--overwrite        Force re-evaluation even if the 'tags' field exists

Environment Dependencies
------------------------
1. python -m pip install openai>=1.13.3
2. Set environment variable OPENAI_API_KEY=<key>
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import os
import sys
import threading
import time
from typing import List, Dict, Any

import openai
from openai import OpenAI
from openai._exceptions import OpenAIError

# ---------------------------------- Configuration ----------------------------------
DEFAULT_INPUT = "_data/filter_papers.json"
DEFAULT_OUTPUT = "_data/tagged_papers.json"
DEFAULT_MODEL = "gpt-4o"
MAX_RETRY = 3
RETRY_BACKOFF_SEC = 5
DEFAULT_API_KEY_FILE = "secrets/api_key.json"

VALID_TAGS = [
    "Verification",
    "Synthesis",
    "P&R",
    "Analog Design",
    "System-level Optimization",
    "Code Generation",
    "Security",
    "Testing",
    "Other",
]

# ------------------------------ Core Functions -----------------------------------

def build_prompt(title: str, abstract: str) -> List[Dict[str, str]]:
    """Constructs the messages required for Chat Completion."""
    system_msg = (
        "You are an expert research assistant specializing in computer architecture and hardware design. "
        "Your task is to assign between one and three most-fitting category tags to academic papers based on their title and abstract.\n\n"
        "The paper is known to be in the 'AI for Systems/Architecture/Hardware' domain. You must choose one to three tags from the following list that best describe the paper's primary contributions. If only one tag fits, provide only one. Do not force multiple tags if they are not relevant.\n"
        f"Available tags: `{'`, `'.join(VALID_TAGS)}`\n\n"
        "Here are explanations for each tag:\n"
        "- **Verification**: Using AI/ML for formal verification, simulation, or validation of hardware designs.\n"
        "- **Synthesis**: Using AI/ML for high-level synthesis (HLS), logic synthesis, or generating hardware from high-level descriptions.\n"
        "- **P&R**: Using AI/ML for physical design tasks like placement, routing, and clock tree synthesis.\n"
        "- **Analog Design**: Using AI/ML for the design, optimization, or layout of analog, RF, or mixed-signal circuits.\n"
        "- **System-level Optimization**: Using AI/ML to optimize system-level concerns like architecture, power, performance, or resource management (e.g., cache policies, NoC routing, memory controllers).\n"
        "- **Code Generation**: Using AI/ML to generate or optimize hardware description languages (e.g., Verilog, VHDL) or related code.\n"
        "- **Security**: Using AI/ML to address hardware security challenges, such as detecting vulnerabilities, side-channel attacks, or Trojans.\n"
        "- **Testing**: Using AI/ML for post-silicon validation, test pattern generation, or fault diagnosis.\n"
        "- **Other**: If the paper's main contribution does not fit well into any of the above categories.\n\n"
        "--- EXAMPLE 1 ---\n"
        'Title: "A Deep-Learning-Based Framework for Routing Congestion Prediction in High-Performance Processors"\n'
        'Abstract: "We propose a novel framework that uses a convolutional neural network to predict routing congestion hotspots early in the physical design flow..."\n'
        "Correct Answer: P&R\n\n"
        "--- EXAMPLE 2 ---\n"
        'Title: "Automated Microarchitectural Design Space Exploration using Reinforcement Learning"\n'
        'Abstract: "This work presents a reinforcement learning agent that navigates the vast design space of modern CPUs, simultaneously optimizing for power and performance by adjusting cache sizes and branch predictor strategies."\n'
        "Correct Answer: System-level Optimization\n\n"
        "--- EXAMPLE 3 ---\n"
        'Title: "Leveraging Large Language Models for Automatic Generation and Verification of RTL Modules"\n'
        'Abstract: "We introduce a novel method where an LLM generates Verilog code from natural language. The same model is then prompted to generate SystemVerilog assertions to create a self-contained verification environment."\n'
        "Correct Answer: Code Generation, Verification\n"
        "--- END OF EXAMPLES ---\n\n"
        "Now, classify the following paper. Respond with one to three tags from the list, separated by commas."
    )

    user_msg = (
        f"Title: {title}\n"
        f"Abstract: {abstract}\n\n"
        "What are the most appropriate tags for this paper? (1-3 tags, comma-separated)"
    )

    return [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_msg},
    ]


def query_model(client: OpenAI, messages: List[Dict[str, str]], model: str = DEFAULT_MODEL) -> str:
    """Calls OpenAI ChatCompletion, returns the result string."""
    for attempt in range(1, MAX_RETRY + 1):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.0,
                max_tokens=40,  # Increased to allow for multiple tags
            )
            ans = response.choices[0].message.content.strip()
            return ans
        except OpenAIError as e:
            if attempt == MAX_RETRY:
                raise
            # Exponential backoff
            wait = RETRY_BACKOFF_SEC * attempt
            print(f"⚠️  OpenAI API error ({e}); retrying in {wait}s…", file=sys.stderr)
            time.sleep(wait)
    # If it still hasn't returned, raise an exception
    raise RuntimeError("Failed to get response from OpenAI API after retries")


def tag_item(client: OpenAI, item: Dict[str, Any], model: str, overwrite: bool = False) -> None:
    """Classifies a single paper record and adds a 'tags' list to it."""
    if not overwrite and "tags" in item:
        return

    messages = build_prompt(item["title"], item["abstract"])
    result_str = query_model(client, messages, model=model)

    # Split the comma-separated string and find all valid tags
    raw_tags = [tag.strip() for tag in result_str.split(',')]
    found_tags = []
    for raw_tag in raw_tags:
        for valid_tag in VALID_TAGS:
            if valid_tag.lower() in raw_tag.lower() and valid_tag not in found_tags:
                found_tags.append(valid_tag)
    
    if not found_tags:
        found_tags.append("Other")

    item["tags"] = found_tags


# ------------------------------ Main Function -----------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Tag papers with 1-3 sub-topics using an OpenAI model")
    parser.add_argument("--input", default=DEFAULT_INPUT, help="Path to the input JSON file of filtered papers")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Path to the output JSON file with tagged papers")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"OpenAI model name (default: {DEFAULT_MODEL})")
    parser.add_argument("--jobs", "-j", type=int, default=20, help="Number of concurrent API requests (default: 20)")
    parser.add_argument("--api-key-file", default=DEFAULT_API_KEY_FILE,
                        help=f"Path to file containing OpenAI API Key (default: {DEFAULT_API_KEY_FILE})")
    parser.add_argument("--overwrite", action="store_true", help="Force re-tagging all papers, ignoring existing ones")

    args = parser.parse_args()

    # --- Load Input Data ---
    if not os.path.isfile(args.input):
        print(f"❌ Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    with open(args.input, "r", encoding="utf-8") as f:
        all_papers = json.load(f)

    # --- Load Existing Tagged Data (if any) ---
    existing_papers = []
    if not args.overwrite and os.path.isfile(args.output):
        try:
            with open(args.output, "r", encoding="utf-8") as f:
                existing_papers = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"⚠️  Could not read existing output file, will overwrite it. Reason: {e}", file=sys.stderr)

    # --- Identify Papers to Process ---
    if args.overwrite:
        items_to_process = all_papers
        print(f"⚠️  --overwrite flag is set. Re-tagging all {len(all_papers)} papers from input.")
    else:
        existing_urls = {item.get("url") for item in existing_papers if item.get("url")}
        items_to_process = [item for item in all_papers if item.get("url") not in existing_urls]

    # --- Prepare OpenAI API Key ---
    if items_to_process:
        if not os.getenv("OPENAI_API_KEY"):
            key_file = args.api_key_file
            if os.path.isfile(key_file):
                try:
                    with open(key_file, "r", encoding="utf-8") as kf:
                        try:
                            key_data = json.load(kf)
                            api_key_val = (
                                key_data.get("OPENAI_API_KEY")
                                or key_data.get("api_key")
                                or key_data.get("key")
                            )
                        except json.JSONDecodeError:
                            kf.seek(0)
                            api_key_val = kf.read().strip()
                        if api_key_val:
                            os.environ["OPENAI_API_KEY"] = api_key_val
                except Exception as e:
                    print(f"⚠️  Failed to read API Key file: {e}", file=sys.stderr)

        if not os.getenv("OPENAI_API_KEY"):
            print(f"❌ OPENAI_API_KEY not found in environment variables or file (tried to read {args.api_key_file})", file=sys.stderr)
            sys.exit(1)

    client = OpenAI()

    # --- Tag New Papers ---
    if not items_to_process:
        print("✓ No new papers to tag.")
        final_data = existing_papers
    else:
        print(f"Found {len(items_to_process)} new papers to tag. Using {args.jobs} concurrent workers...")
        processed_count = 0
        total_to_process = len(items_to_process)
        lock = threading.Lock()

        def process_wrapper(item: Dict[str, Any]) -> None:
            nonlocal processed_count
            try:
                tag_item(client, item, args.model, overwrite=True)  # Always overwrite as we only process new items
            except Exception as e:
                print(f"⚠️  Tagging failed for '{item.get('title', 'N/A')}', skipping: {e}", file=sys.stderr)
                item["tags"] = ["Error"]
            finally:
                with lock:
                    processed_count += 1
                    if processed_count % 10 == 0 or processed_count == total_to_process:
                        print(f"  Processed {processed_count}/{total_to_process} papers...")

        with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as executor:
            executor.map(process_wrapper, items_to_process)
        
        # Combine and set final data
        final_data = existing_papers + items_to_process

    # --- Sort and Save ---
    print("Sorting all papers by publication date...")
    final_data.sort(key=lambda x: x.get("published", ""), reverse=True)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(final_data, f, indent=2, ensure_ascii=False)

    print(f"✓ Tagging complete. Total {len(final_data)} papers saved to → {args.output}")


if __name__ == "__main__":
    main() 