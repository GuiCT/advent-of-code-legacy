from re import S


whole_input: str
with open("../input.txt", "r") as f:
    whole_input = f.read()

def surface_area(l: int, w: int, h: int) -> int:
    smallest_product = min(l * w, w * h, h * l)
    return 2 * l * w + 2 * w * h + 2 * h * l + smallest_product

def ribbon(l: int, w: int, h: int) -> int:
    smallest_sides = [l, w, h]
    smallest_sides.sort()
    smallest_sides = smallest_sides[:2]
    return sum(smallest_sides) * 2 + l * w * h


# Part 1: sum of the surface area for each box
# Part 2: amount of ribbon (smallest perimeter + product of 3 sides)
net: int = 0
net_ribbon: int = 0
for line in whole_input.splitlines():
    l, w, h = line.split("x")
    l = int(l)
    w = int(w)
    h = int(h)
    net += surface_area(l, w, h)
    net_ribbon += ribbon(l, w, h)
print(f"Sum is equal to {net}")
print(f"Ribbon sum is equal to {net_ribbon}")
