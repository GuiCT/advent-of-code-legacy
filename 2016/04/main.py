import re
from collections import Counter
from functools import cmp_to_key

PARSE_REGEX = re.compile(r"^(.+)-(\d+)\[(.*)\]$")


def parse_input(row: str):
    has_match = PARSE_REGEX.match(row)
    if has_match:
        text, id, validator = has_match.groups()
        text = text.replace("-", "")
        return text, int(id), validator
    raise ValueError(f"Invalid text for row: {row}")


def sort_counter(item1: tuple[str, int], item2: tuple[str, int]) -> int:
    if item1[1] == item2[1]:
        return ord(item1[0]) - ord(item2[0])
    return item2[1] - item1[1]


def validate_room(text: str, _:int, validator: str) -> bool:
    most_common_letters = Counter(text).most_common()
    key_func = cmp_to_key(sort_counter)
    most_common_letters.sort(key=key_func)
    most_common_letters = most_common_letters[:5]
    most_common_letters = [letter for letter, _ in most_common_letters]
    most_common_letters = "".join(most_common_letters)
    return most_common_letters == validator


def cycle_alphabet(letter: str, shift: int) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    index = (alphabet.index(letter) + shift) % len(alphabet)
    return alphabet[index]


def decrypt_input(input: str, id: int) -> str:
    curr = input.replace("-", " ")
    curr = [cycle_alphabet(letter, id) for letter in curr]
    return "".join(curr)

with open("input.txt", "r") as f:
    lines = f.readlines()
    rooms = [room for room in map(parse_input, lines)]
    valid_rooms = [room for room in rooms if validate_room(*room)]
    count = sum(room[1] for room in valid_rooms)
    print("Part 1 answer: ", count)
    for room in valid_rooms:
        decrypted = decrypt_input(room[0], room[1])
        if "north" in decrypted:
            print("Part 2 answer: ", room[1], ", at room", f"{room[0]}-{room[1]}[{room[2]}]")
            print("Decrypted: ", decrypted)
            break