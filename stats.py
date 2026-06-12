def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)



def get_chars_dict(text: str) -> dict[str, int]:
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]


def character_sorted(character_dict: dict[str, int]) -> list:
    char_sorted = []
    for char in character_dict:
        if char.isalpha():
            char_sorted.append({"char": char, "count": character_dict[char]})
    char_sorted.sort(reverse=True, key=sort_on)
    return char_sorted


