import numpy as np

whole_input: str
with open("../input.txt", "r") as f:
    whole_input = f.read()


def parse_line(line: str):
    splits = line.split(" ")
    match len(splits):
        case 4:
            action = splits[0].upper()
            splits.pop(0)
        case 5:
            action = splits[1].upper()
            splits.pop(0)
            splits.pop(0)
        case _:
            raise ValueError("Deu ruim")
    x_start, y_start = splits[0].split(",")
    x_end, y_end = splits[2].split(",")
    x_start = int(x_start)
    y_start = int(y_start)
    x_end = int(x_end)
    y_end = int(y_end)
    return action, x_start, y_start, x_end, y_end


matrix = np.full((1000, 1000), False)
lines = whole_input.splitlines()
# Part one: how many lights are lit
for line in lines:
    action, x_start, y_start, x_end, y_end = parse_line(line)
    match action:
        case "ON":
            matrix[x_start:x_end + 1, y_start:y_end + 1] = True
        case "OFF":
            matrix[x_start:x_end + 1, y_start:y_end + 1] = False
        case "TOGGLE":
            old = matrix[x_start:x_end + 1, y_start:y_end + 1]
            new = np.invert(old)
            matrix[x_start:x_end + 1, y_start:y_end + 1] = new
        case _:
            raise ValueError("Deu ruim")
count_true = np.count_nonzero(matrix)
print(f"Part 1 result: {count_true}")

# Part two: total brightness
matrix = np.full((1000, 1000), 0)
# Decrease value by one but keeps minimum of 0
def safe_decrease(current: int) -> int:
    return np.maximum(current - 1, 0)
safe_decrease = np.vectorize(safe_decrease)
for line in lines:
    action, x_start, y_start, x_end, y_end = parse_line(line)
    match action:
        case "ON":
            matrix[x_start:x_end + 1, y_start:y_end + 1] += 1
        case "OFF":
            new = safe_decrease(matrix[x_start:x_end + 1, y_start:y_end + 1])
            matrix[x_start:x_end + 1, y_start:y_end + 1] = new
        case "TOGGLE":
            matrix[x_start:x_end + 1, y_start:y_end + 1] += 2
        case _:
            raise ValueError("Deu ruim")
total_brightness = np.sum(matrix)
print(f"Part 2 result: {total_brightness}")