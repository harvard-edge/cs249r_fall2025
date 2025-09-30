import json
import os

def shuffle_and_sort_papers():
    """
    Reads papers from a JSON file, sorts them by publication date in descending order,
    and writes the sorted list back to the file.
    """
    # Construct the path to the data file relative to the script's location
    scripts_dir = os.path.dirname(__file__)
    data_file_path = os.path.join(scripts_dir, '..', '_data', 'filter_papers.json')

    try:
        # Read the papers from the JSON file
        with open(data_file_path, 'r', encoding='utf-8') as f:
            papers = json.load(f)

        # Sort the papers by the 'published' date in descending order
        # The 'published' field is an ISO 8601 string, which can be sorted lexicographically.
        papers.sort(key=lambda x: x.get('published', ''), reverse=True)

        # Write the sorted papers back to the same file
        with open(data_file_path, 'w', encoding='utf-8') as f:
            json.dump(papers, f, indent=2, ensure_ascii=False)

        print(f"Successfully sorted {len(papers)} papers in '{data_file_path}' by publication date.")

    except FileNotFoundError:
        print(f"Error: The file '{data_file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from the file '{data_file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    shuffle_and_sort_papers()
