from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    char = {}
    keys = char.keys()
    vals = char.values()
    for c in word:
        if c not in char:
            char[c] = 0
        char[c] += 1
    return char





# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
