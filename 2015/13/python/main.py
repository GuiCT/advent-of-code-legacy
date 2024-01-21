from itertools import permutations
import re


def parse_line(line: str) -> tuple[str, str, int]:
    pattern = re.compile(
        r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).\n')
    match = pattern.match(line)
    if match:
        person_1 = match.group(1)
        person_2 = match.group(4)
        signal = 1 if match.group(2) == 'gain' else -1
        weight = signal * int(match.group(3))
        return person_1, person_2, weight
    else:
        raise ValueError(f'Could not parse line: {line}')


with open('../input.txt', 'r') as file:
    lines = file.readlines()
happinesses: dict[str, dict[str, int]] = dict()
for line in lines:
    person_1, person_2, weight = parse_line(line)
    current_dict = happinesses.get(person_1, None)
    if current_dict is None:
        current_dict = dict()
        current_dict[person_2] = weight
        happinesses[person_1] = current_dict
    else:
        current_dict[person_2] = weight
# Computing the default permutation
persons = list(happinesses.keys())
num_persons = len(persons)

# Computing every single permutation (brute-forcing)
max_happiness = 0
for permutation in permutations(persons):
    happiness = 0
    for i in range(num_persons):
        target = permutation[i]
        prev_name = permutation[(i - 1) % num_persons]
        next_name = permutation[(i + 1) % num_persons]
        happiness += happinesses[target][prev_name] + \
            happinesses[target][next_name]
    max_happiness = max(max_happiness, happiness)
print(f"[Part 1] Optimal happiness: {max_happiness}")

# Part 2: Including myself
me_dict: dict[str, int] = dict()
for person in persons:
    me_dict[person] = 0
    happinesses[person]['Me'] = 0
happinesses['Me'] = me_dict
persons = list(happinesses.keys())
num_persons = len(persons)

# Computing every single permutation (brute-forcing)
max_happiness = 0
for permutation in permutations(persons):
    happiness = 0
    for i in range(num_persons):
        target = permutation[i]
        prev_name = permutation[(i - 1) % num_persons]
        next_name = permutation[(i + 1) % num_persons]
        happiness += happinesses[target][prev_name] + \
            happinesses[target][next_name]
    max_happiness = max(max_happiness, happiness)
print(f"[Part 2] Optimal happiness: {max_happiness}")
