import re


PATTERN = re.compile(r'([a-zA-Z]+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.')
TOTAL_TIME = 2503


def parse_line(line: str) -> tuple[str, int, int, int]:
    res = PATTERN.match(line)
    groups = res.groups()
    return (groups[0], int(groups[1]), int(groups[2]), int(groups[3]))


with open('../input.txt', 'r') as file:
    lines = file.readlines()

current_winning_distance = 0
for line in lines:
    name, speed, duration, resting_time = parse_line(line)
    time = 0
    distance = 0
    is_resting = False
    while time < TOTAL_TIME:
        remaining = TOTAL_TIME - time
        if is_resting:
            time += resting_time
            is_resting = False
        else:
            time_flying = min(duration, remaining)
            distance += time_flying * speed
            time += time_flying
            is_resting = True
    if distance > current_winning_distance:
        current_winning_distance = distance

print(f"Winning distance: {current_winning_distance}")
