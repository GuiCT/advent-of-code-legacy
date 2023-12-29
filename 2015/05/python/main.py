whole_input: str
with open("../input.txt", "r") as f:
    whole_input = f.read()

VOWELS = ["a", "e", "i", "o", "u"]
PART1_BAD_STRINGS = ["ab", "cd", "pq", "xy"]


def part1_check(string: str) -> bool:
    vowels: list[str] = list()
    has_double_letter = False
    for bad_string in PART1_BAD_STRINGS:
        if bad_string in string:
            return False
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            has_double_letter = True
        if string[i] in VOWELS:
            vowels.append(string[i])
    if string[-1] in VOWELS:
        vowels.append(string[-1])
    return len(vowels) >= 3 and has_double_letter


assert part1_check("ugknbfddgicrmopn") == True
assert part1_check("aaa") == True
assert part1_check("jchzalrnumimnmhp") == False
assert part1_check("haegwjzuvuyypxyu") == False
assert part1_check("dvszwmarrgswjxmb") == False


def part2_check(string: str) -> bool:
    pairs: set[str] = set()
    has_duplicate_pair = False
    has_letter_sandwich = False
    # Two passes, because yes
    for i in range(len(string) - 2):
        if string[i] == string[i + 2]:
            has_letter_sandwich = True
            break
    i = 0
    while i < len(string) - 2:
        if string[i: i + 2] in pairs:
            has_duplicate_pair = True
            break
        else:
            if string[i: i + 2] == string[i + 1: i + 3]:
                pairs.add(string[i: i + 2])
                i += 2
                continue
            else:
                pairs.add(string[i: i + 2])
        i += 1
    if i == len(string) - 2:
        if string[i: i + 2] in pairs:
            has_duplicate_pair = True
    return has_duplicate_pair and has_letter_sandwich


assert part2_check("xyxy") == True
assert part2_check("aabcdefgaa") == False
assert part2_check("aaa") == False
assert part2_check("qjhvhtzxzqqjkmpb") == True
assert part2_check("xxyxx") == True
assert part2_check("uurcxstgmygtbstg") == False
assert part2_check("ieodomkazucvgmuy") == False

count_part_1 = 0
count_part_2 = 0
for line in whole_input.splitlines():
    if part1_check(line):
        count_part_1 += 1
    if part2_check(line):
        count_part_2 += 1
print(f"Part 1 count: {count_part_1}")
print(f"Part 2 count: {count_part_2}")
