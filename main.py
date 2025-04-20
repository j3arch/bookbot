import sys
from stats import count_words
from stats import character_count
from stats import character_sorted



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_text = get_book_text(sys.argv[1])
    char_list = character_count(book_text)
    num_words = count_words(book_text)
    sorted_chars = character_sorted(char_list)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")
    
    print("============= END ===============")



def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()



