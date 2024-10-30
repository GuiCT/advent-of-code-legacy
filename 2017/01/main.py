import re


with open("input.txt", "r") as f:
    file_str = f.read()

repeated = re.sub(r"(\d)(\1*)", r"\2", file_str)
print(repeated)
last_repeats = file_str[-1] == file_str[0]

sum_str = 0
for ch in repeated:
    sum_str += int(ch)

if last_repeats:
    sum_str += int(file_str[-1])

print("Part 1", sum_str)

sum_str = 0
steps = len(file_str) // 2
# dumb way to solve go, fvck regex.
for i in range(len(file_str)):
    next_char_idx = (i + steps) % len(file_str)
    if file_str[i] == file_str[next_char_idx]:
        sum_str += int(file_str[i])

print("Part 2", sum_str)