def count_words(book_text: str) -> int:
    word_count = len(book_text.split())
    return word_count



def character_count(book_text: str) -> dict[str, int]:
    character_list = {}
    book_text = book_text.lower()
    for char in book_text:
        if char in character_list: 
            character_list[char] += 1
        else:
            character_list[char] = 1
    return character_list


def sort_on(item) -> int:
        return item["count"]

def character_sorted(character_dict: dict[str, int]) -> list:
    char_sorted = []
    for char in character_dict:
        if char.isalpha():
            char_sorted.append({"char": char, "count": character_dict[char]})
    char_sorted.sort(reverse=True, key=sort_on)
    return char_sorted


