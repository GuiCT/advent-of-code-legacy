import re

things = [
        'children', 'cats', 'samoyeds', 'pomeranians', 'akitas', 'vizslas',
        'goldfish', 'trees', 'cars', 'perfumes'
        ]

target = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
}

aunts = []

possibles = []

def read_data():
    with open("input.txt", 'r') as f:
        for l in f:
            s = l.split()
            a = [int(s[1])]
            for i in range(2, len(s), 2):
                a.append((s[i], int(s[i+1])))
            aunts.append(a)


    for x in aunts:
        for c in x[1:]:
            if target[c[0]] == c[1] and c[0] not in ["cats", "trees", "pomeranians", "goldfish"] :
                continue
            elif c[0] in ["cats", "trees"]:
                if target[c[0]] >= c[1]:
                    continue
                else:
                    break
            elif c[0] in ["pomeranians", "goldfish"]:
                if target[c[0]] <= c[1]:
                    continue
                else:
                    break
            else:
                break
        else:
            possibles.append(x)

    for y in possibles:
        print(y)