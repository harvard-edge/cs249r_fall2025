#!/bin/bash
set -e

echo "Running arxiv_manager_min.py..."
python3 scripts/arxiv_manager_min.py --mode 1

echo "Running classify_papers.py..."
python3 scripts/classify_papers.py 

echo "Running shuffle_papers.py..."
python3 scripts/shuffle_papers.py

echo "Running tag_papers.py..."
python3 scripts/tag_papers.py

echo "All scripts executed successfully!"
