import json

with open("input.txt", "r") as f:
    data = json.load(f)

def sum_numbers(data):
    if isinstance(data, dict):
        if "red" in data.values():
            return 0
        return sum(map(sum_numbers, data.values()))
    if isinstance(data, list):
        return sum(map(sum_numbers, data))
    if isinstance(data, int):
        return data
    return 0

print("Part 2 value:")
print(sum_numbers(data))
