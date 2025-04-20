def count_words(book_text):
    word_count = len(book_text.split())
    return word_count



def character_count(book_text):
    character_list = {}
    book_text = book_text.lower()
    for char in book_text:
        if char in character_list: 
            character_list[char] += 1
        else:
            character_list[char] = 1
    return character_list


def sort_on(item):
        return item["count"]

def character_sorted(character_dict):
    char_sorted = []
    for char in character_dict:
        if char.isalpha():
            char_sorted.append({"char": char, "count": character_dict[char]})
    char_sorted.sort(reverse=True, key=sort_on)
    return char_sorted


