with open("input.txt", "r") as f:
    lines = f.readlines()


matrix = []
for l in lines:
    this_row_entries_str = l.strip().split("\t")
    this_row_as_int = list(map(lambda s: int(s), this_row_entries_str))
    matrix.append(this_row_as_int)

sum_val = 0
for row in matrix:
    min_val = row[0]
    max_val = row[0]
    for entry in row[1:]:
        if entry < min_val:
            min_val = entry
        if entry > max_val:
            max_val = entry
    sum_val += (max_val - min_val)

print("Part 1", sum_val)


def find_divisor_within(target: int, candidates: list[int]) -> int | None:
    for entry in candidates:
        if target % entry == 0:
            return entry
    return None


def find_division_in_row(row: list[int]) -> int | None:
    for i in range(len(row)):
        head = row[i]
        divisors_candidates = row.copy()
        divisors_candidates.pop(i)
        divisor = find_divisor_within(head, divisors_candidates)
        if divisor is not None:
            return head // divisor
    return None


sum_val_2 = 0
for row in matrix:
    row_division_found = find_division_in_row(row)
    if row_division_found is not None:
        sum_val_2 += row_division_found

print("Part 2", sum_val_2)