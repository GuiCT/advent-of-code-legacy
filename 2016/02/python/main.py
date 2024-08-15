with open("input.txt", "r") as f:
    lines = f.readlines()


matrix_part1 = [
    ["1",   "2",    "3"],
    ["4",   "5",    "6"],
    ["7",   "8",    "9"]
]

curr_x, curr_y = 1, 1
code = str()


def get_actions(matrix: list[list[str]]):
    max_x, max_y = len(matrix[0]) - 1, len(matrix) - 1
    return {
        "U": lambda x, y: (x, max(0, y - 1)),
        "R": lambda x, y: (min(max_x, x + 1), y),
        "D": lambda x, y: (x, min(max_y, y + 1)),
        "L": lambda x, y: (max(0, x - 1), y)
    }


actions_part1 = get_actions(matrix_part1)
for line in lines:
    for char in line.strip():
        curr_x, curr_y = actions_part1[char](curr_x, curr_y)
    code += matrix_part1[curr_y][curr_x]

print(f"Part 1 result is {code}")

# Part 2

matrix_part2 = [
    [None,  None,   "1",    None,   None],
    [None,  "2",    "3",    "4",    None],
    ["5",   "6",    "7",    "8",    "9"],
    [None,  "A",    "B",    "C",    None],
    [None,  None,   "D",    None,   None],
]


curr_x, curr_y = 0, 2
code_part2 = str()


def move_if_valid(x, y, action, matrix):
    new_x, new_y = action(x, y)
    is_valid = matrix[new_y][new_x] is not None
    return (new_x, new_y) if is_valid else (x, y)

actions_part2 = get_actions(matrix_part2)
for line in lines:
    for char in line.strip():
        curr_x, curr_y = move_if_valid(curr_x, curr_y, actions_part2[char], matrix_part2)
    code_part2 += matrix_part2[curr_y][curr_x]

print(f"Part 2 result is {code_part2}")
