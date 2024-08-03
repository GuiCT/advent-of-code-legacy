import re

things = {
    'children': '==',
    'cats': '>',
    'samoyeds': '==',
    'pomeranians': '<',
    'akitas': '==',
    'vizslas': '==',
    'goldfish': '<',
    'trees': '>',
    'cars': '==',
    'perfumes': '=='
}

target = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

aunt_pattern = re.compile(
    r"Sue (\d+): ([a-zA-Z]+): (\d+), ([a-zA-Z]+): (\d+), ([a-zA-Z]+): (\d+)")

with open("input.txt") as f:
    for line in f:
        match = aunt_pattern.match(line)
        if match:
            comparisons_keys = match.groups()[1::2]
            comparisons_values = map(int, match.groups()[2::2])
            comparisons_ops = map(things.get, comparisons_keys)
            aunt = dict(zip(comparisons_keys, comparisons_values))
            if all(
                eval(
                    f"{aunt[key]} {op} {target[key]}"
                ) for key, op in zip(comparisons_keys, comparisons_ops)
            ):
                print(match.groups()[0])
