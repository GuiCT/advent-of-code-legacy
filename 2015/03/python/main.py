whole_input: str
with open("../input.txt", "r") as f:
    whole_input = f.read()

# Part 1: keep track of every house, (0, 0) is assumed to be within the dict, as
# it is the starting point
visited_houses: dict[tuple[int, int], int] = dict()
current = (0, 0)
for move in whole_input:
    visited_houses[current] = visited_houses.get(current, 0) + 1
    if move == "^":
        current = (current[0], current[1] + 1)
    elif move == "v":
        current = (current[0], current[1] - 1)
    elif move == ">":
        current = (current[0] + 1, current[1])
    elif move == "<":
        current = (current[0] - 1, current[1])
    else:
        raise ValueError(f"Invalid move: {move}")
# Last house
visited_houses[current] = visited_houses.get(current, 0) + 1
print(f"Houses with AT LEAST ONE: {len(visited_houses)}")

# Part 2: Robo-Santa will take the even moves, Santa will take the odd moves
visited_houses = dict()
current_santa = (0, 0)
current_robo = (0, 0)
i = 0
while i < len(whole_input) - 1:
    visited_houses[current_santa] = visited_houses.get(current_santa, 0) + 1
    visited_houses[current_robo] = visited_houses.get(current_robo, 0) + 1
    move_santa = whole_input[i]
    move_robo = whole_input[i + 1]
    if move_santa == "^":
        current_santa = (current_santa[0], current_santa[1] + 1)
    elif move_santa == "v":
        current_santa = (current_santa[0], current_santa[1] - 1)
    elif move_santa == ">":
        current_santa = (current_santa[0] + 1, current_santa[1])
    elif move_santa == "<":
        current_santa = (current_santa[0] - 1, current_santa[1])
    else:
        raise ValueError(f"Invalid move: {move_santa}")
    if move_robo == "^":
        current_robo = (current_robo[0], current_robo[1] + 1)
    elif move_robo == "v":
        current_robo = (current_robo[0], current_robo[1] - 1)
    elif move_robo == ">":
        current_robo = (current_robo[0] + 1, current_robo[1])
    elif move_robo == "<":
        current_robo = (current_robo[0] - 1, current_robo[1])
    else:
        raise ValueError(f"Invalid move: {move_robo}")
    i += 2
if i == len(whole_input) - 1:
    visited_houses[current] = visited_houses.get(current, 0) + 1
print(f"Part 2, with Robo-Santa help: {len(visited_houses)}")