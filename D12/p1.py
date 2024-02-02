from itertools import product

def is_row_valid(row: list[str], expected_groups: list[int]) -> bool:
    groups = []
    current_group = 0
    for c in row:
        if c == "#":
            current_group += 1
        elif current_group > 0:
            groups.append(current_group)
            current_group = 0
    if current_group > 0:
        groups.append(current_group)
    return groups == expected_groups

def apply_permutation(row: list[str], permutation: list[str]) -> str:
    new_row = row.copy()
    for i, c in enumerate(new_row):
        if c == "?":
            new_row[i] = permutation.pop()
    return new_row

def count_valid_permutations(row: list[str], expected_groups: list[int]):
    num_free_slots = row.count("?")
    # Brute force method has 2^num_free_slots complexity but num_free_slots is always sufficiently low that we can deal with this
    permutation_validity = map(lambda r: is_row_valid(r, expected_groups), map(lambda p: apply_permutation(list(row), list(p)), product(".#", repeat=num_free_slots)))
    return len(list(filter(None, permutation_validity)))

def process_raw_row(raw_row: str) -> int:
    springs, raw_groups = raw_row.split()

    row = list(springs)

    expected_groups = list(map(int, raw_groups.split(",")))

    return count_valid_permutations(row, expected_groups)
    
with open("D12/data") as f:
    raw_rows = f.readlines()

    print(sum(map(process_raw_row, raw_rows)))
