#!/usr/bin/env python3
"""
arxiv_manager_min.py — 维护 “LLM for hardware design” 相关论文的 JSON 清单。

用法
-----
# 第一次拉取全部结果（会覆盖旧 JSON）
python arxiv_manager_min.py --mode 0

# 之后按需增量更新（只追加新论文）
python arxiv_manager_min.py --mode 1

可选参数
--------
--output FILE      输出 JSON 路径（默认为 llm_hw_design_papers.json）
--query  STRING    自定义检索词
--max-results N    最多检索条数（默认 2000）

依赖
----
pip install arxiv>=2.0.0
"""

import argparse
import json
import os
from datetime import datetime, timezone

# 需要 arxiv 2.x
import arxiv
# 当 arXiv API 某一分页意外为空时会抛出此异常
from arxiv import UnexpectedEmptyPageError

# 默认检索关键词集合（可按需修改）
# DEFAULT_QUERIES = [
#     '(LLM OR "large language model") AND "hardware design"',
#     '"generative ai" AND fpga',
#     '"large language model" AND "circuit design"',
#     '(LLM OR "large language model") AND verilog',
# ]

# --------- arXiv 关键词配置 ---------
# --------- arXiv 关键词配置（v3：含 CUDA & AI/ML）---------
# --------- arXiv 关键词配置（v4：加入 *learning* 同义词）---------
DEFAULT_QUERIES = [
    # 原有（已验证）的7条：
    '(GPT OR ChatGPT OR Codex OR "foundation model") AND ("hardware design")',
    '(learning OR ai) AND ("hardware design")',
    '(LLM OR "large language model") AND (ASIC OR chip OR EDA OR "electronic design automation")',
    '(learning OR ai) AND (ASIC OR chip OR EDA OR "electronic design automation")',
    '(LLM OR GPT) AND ("hardware description language" OR HDL OR Verilog OR VHDL OR Chisel OR SystemVerilog)',
    '(learning OR ai) AND ("hardware description language" OR HDL OR Verilog OR VHDL OR Chisel OR SystemVerilog)',
    '(LLM OR GPT) AND ("design space exploration" OR "design verification" OR testbench)',
    '(learning OR ai) AND ("design space exploration" OR "design verification" OR testbench)',
    '(LLM OR GPT) AND ("physical design" OR "place and route" OR "timing closure")',
    '(learning OR ai) AND ("physical design" OR "place and route" OR "timing closure")',
    '(LLM OR "generative AI") AND ("bug fixing" AND (Verilog OR VHDL))',
    '(learning OR ai) AND ("bug fixing" AND (Verilog OR VHDL))',
    '(LLM OR GPT) AND ("design automation" OR "hardware code generation" OR "HDL generation")',
    '(learning OR ai) AND ("design automation" OR "hardware code generation" OR "HDL generation")',

    # 新增的（风格和原版保持一致的几条扩展）：
    '(LLM OR GPT) AND (analog)',
    '(LLM OR GPT) AND (system OR architecture)',
    '(LLM OR GPT) AND (CUDA OR GPU)',
    '(LLM OR GPT) AND (code OR software OR program)',
]



# ------------------------------------------------------------------

# -------------------------------------------------------------------------

# -----------------------------------


DEFAULT_OUTPUT = "_data/llm_hw_design_papers.json"
DEFAULT_MAX_RESULTS = 2000


def fetch_papers(query: str, max_results: int = DEFAULT_MAX_RESULTS):
    """
    迭代返回符合查询的 arXiv 结果字典（按发表时间倒序）。

    使用 arxiv.Client 取代已弃用的 Search.results()
    """
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    client = arxiv.Client(
        page_size=100,      # 每次 API 调用返回条数
        delay_seconds=3,    # 遵守 arXiv 速率限制
    )

    count = 0
    try:
        for result in client.results(search):
            if count == 0:
                print(f'  Fetching for "{query}"...')
            count += 1
            if count > 0 and count % 100 == 0:
                print(f"  ... fetched {count} results so far.")
            yield {
                "title": result.title.strip(),
                "url": result.entry_id,
                "abstract": result.summary.strip().replace("\n", " "),
                "published": result.published.replace(tzinfo=timezone.utc)
                             .strftime("%Y-%m-%dT%H:%M:%SZ"),
            }
        
        if count > 0:
            print(f"  Finished query. Found {count} papers.")
        else:
            print(f"  No results for query.")

    except UnexpectedEmptyPageError as e:
        # 某些分页可能因 arXiv API 状态异常返回空白，此时直接跳过当前关键词
        # 在 arxiv >= 2.1.0 中，当结果总数是 page_size 的整数倍时，
        # 在取完最后一页后会触发此“异常”，但这属于正常行为。
        # 我们在此处捕获它并直接忽略，以允许生成器正常退出。
        print(f"  Query finished (hit an empty page). Found {count} papers.")
        pass
    except Exception as e:
        # 捕获其它未知错误，保证脚本不中断
        print(f"⚠️  检索 [{query}] 时发生错误，已跳过：{e}")


def load_existing(path: str):
    """读取已有 JSON，返回列表和已存在的 URL 集合。"""
    if not os.path.isfile(path):
        return [], set()
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data, {item["url"] for item in data}


def save_json(path: str, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✓ 写入 {len(data)} 条记录 → {path}")


def main():
    parser = argparse.ArgumentParser(description="Manage arXiv papers list")
    parser.add_argument("--mode", type=int, choices=[0, 1], required=True,
                        help="0 = 全量重建, 1 = 增量追加")
    parser.add_argument("--output", default=DEFAULT_OUTPUT,
                        help="输出 JSON 文件路径")
    # --query 可以重复出现以提供多组关键词
    parser.add_argument("--query", action="append",
                        help="自定义检索词（可重复使用）。若省略则使用脚本内置的默认集合。")
    parser.add_argument("--max-results", type=int, default=DEFAULT_MAX_RESULTS,
                        help="最大检索条数（默认 2000）")
    args = parser.parse_args()

    # 若未显式提供 --query，则使用脚本预设 DEFAULT_QUERIES
    queries = args.query if args.query else DEFAULT_QUERIES

    print("Querying arXiv with the following term(s):")
    for q in queries:
        print(f"  - {q}")

    # 依次执行多组查询，并按 URL 去重
    new_items = []
    seen_urls = set()
    total_queries = len(queries)
    for i, q in enumerate(queries):
        print(f"\n--- Running query {i+1}/{total_queries} ---")
        for item in fetch_papers(q, args.max_results):
            if item["url"] in seen_urls:
                continue
            new_items.append(item)
            seen_urls.add(item["url"])

    print(f"\nTotal unique papers fetched: {len(new_items)}")
    # 按发布时间倒序排列（ISO 字符串直接比较即可）
    new_items.sort(key=lambda x: x["published"], reverse=True)

    if args.mode == 0:
        # 覆盖写入
        print(f"Mode 0: Saving {len(new_items)} papers (overwrite)...")
        save_json(args.output, new_items)
        return

    # mode == 1 → 读旧文件，去重后追加
    print(f"\nMode 1: Merging with existing file at {args.output}...")
    existing_data, existing_urls = load_existing(args.output)
    print(f"Loaded {len(existing_data)} existing papers.")
    
    add_count = 0
    merged = []

    # 先把新的（不在 existing_urls 的）条目放到前面
    for item in new_items:
        if item["url"] not in existing_urls:
            merged.append(item)
            add_count += 1

    merged.extend(existing_data)  # 旧记录放后面
    if add_count == 0:
        print("没有发现新论文，JSON 未修改。")
    else:
        print(f"Adding {add_count} new papers.")
        save_json(args.output, merged)


if __name__ == "__main__":
    main()
