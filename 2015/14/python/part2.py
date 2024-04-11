import re


PATTERN = re.compile(r'([a-zA-Z]+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds.')
TOTAL_TIME = 2503


def parse_line(line: str) -> tuple[str, int, int, int]:
    res = PATTERN.match(line)
    groups = res.groups()
    return (groups[0], int(groups[1]), int(groups[2]), int(groups[3]))


with open('../input.txt', 'r') as file:
    lines = file.readlines()

reindeers = list()
for line in lines:
    this_reindeer = parse_line(line)
    reindeers.append(this_reindeer)

distance = [0] * len(reindeers)
points = [0] * len(reindeers)
buffer = [reindeer[2] for reindeer in reindeers]
rest = [False] * len(reindeers)

for time in range(TOTAL_TIME):
    leaders_idx = []
    leader_dist = 0
    for i in range(len(reindeers)):
        if not rest[i]:
            distance[i] += reindeers[i][1]
        buffer[i] -= 1
        if buffer[i] == 0:
            rest[i] = not rest[i]
            buffer[i] = reindeers[i][2] if not rest[i] else reindeers[i][3]
        if distance[i] > leader_dist:
            leaders_idx = [i]
            leader_dist = distance[i]
        elif distance[i] == leader_dist:
            leaders_idx.append(i)
    for idx in leaders_idx:
        points[idx] += 1

sorted = points.copy()
sorted.sort()
print(f"Highest point count is: {sorted[-1]}")
