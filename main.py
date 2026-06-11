import sys
from stats import (
    count_words,
    character_count,
    character_sorted
)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
        
    book_text = get_book_text(sys.argv[1])
    char_list = character_count(book_text)
    num_words = count_words(book_text)
    sorted_chars = character_sorted(char_list)
    print_report(book_path, num_words, chars_sorted_list)

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(
    book_path: str, num_words: int, chars_sorted_list: list[tuple[str, int]]
) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in chars_sorted_list:
        if not char.isalpha():
            continue
        print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()



