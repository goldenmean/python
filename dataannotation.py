import requests
import re

def fetch_document(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch document. Status code: {response.status_code}")

def parse_document(content):
    # Regular expression to match lines like "U+2588 at (0,0)"
    pattern = re.compile(r'U\+([0-9A-F]+) at \((\d+),(\d+)\)')
    matches = pattern.findall(content)
    return [(chr(int(char_code, 16)), int(x), int(y)) for char_code, x, y in matches]

def create_grid(characters):
    if not characters:
        return []

    max_x = max(characters, key=lambda item: item[1])[1]
    max_y = max(characters, key=lambda item: item[2])[2]

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for char, x, y in characters:
        grid[y][x] = char

    return grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def main(url):
    document_content = fetch_document(url)
    #print(document_content)
    characters = parse_document(document_content)
    print(characters)
    #grid = create_grid(characters)
    #print_grid(grid)

if __name__ == "__main__":
    url = "https://docs.google.com/document/u/0/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub?pli=1"
    main(url)