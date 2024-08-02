import networkx
import re

PATTERN = re.compile(r"(\w+) to (\w+) = (\d+)")

with open("input.txt", "r") as f:
    lines = f.readlines()

G = networkx.Graph()
for line in lines:
    city_source, city_destination, weight = PATTERN.match(line).groups()
    if city_source not in G:
        G.add_node(city_source)
    if city_destination not in G:
        G.add_node(city_destination)
    G.add_edge(city_source, city_destination, weight=int(weight))

all_simple_paths = []
for i in G:
    for j in G:
        if i != j:
            all_simple_paths.extend(networkx.simple_paths.all_simple_paths(G, i, j))

all_eligible_paths = [path for path in all_simple_paths if len(path) == len(G)]
all_weights_sums = [sum([G[path[i]][path[i+1]]['weight'] for i in range(len(path)-1)]) for path in all_eligible_paths]
print("Part 1:", min(all_weights_sums))
print("Part 2:", max(all_weights_sums))