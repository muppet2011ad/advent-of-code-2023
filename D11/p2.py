from itertools import combinations

type Coord = tuple[int, int]

def get_all_galaxies(image: list[list[str]]) -> list[Coord]:
    galaxies = []
    for x in range(len(image)):
        for y in range(len(image[x])):
            if image[x][y] == "#":
                galaxies.append((x, y))
    return galaxies

def get_all_populated_rows(galaxies: list[Coord]) -> set[int]:
    return set(map(lambda g: g[0], galaxies))

def get_all_populated_columns(galaxies: list[Coord]) -> set[int]:
    return set(map(lambda g: g[1], galaxies))

def calculate_new_location(galaxy: Coord, empty_rows: set[int], empty_columns: set[int]) -> Coord:
    num_new_rows = len(list(filter(lambda r: r < galaxy[0], empty_rows)))
    num_new_cols = len(list(filter(lambda c: c < galaxy[1], empty_columns)))

    return (galaxy[0] + num_new_rows*int(1e6-1), galaxy[1] + num_new_cols*int(1e6-1))

def manhatten_distance(first: Coord, second: Coord) -> int:
    return abs(first[0] - second[0]) + abs(first[1] - second[1])

with open("D11/data") as f:
    image = list(map(list, f.readlines()))

    galaxies = get_all_galaxies(image)

    empty_rows = set(range(len(image))) - get_all_populated_rows(galaxies)
    empty_columns = set(range(len(image[0]))) - get_all_populated_columns(galaxies)

    expanded_galaxies = map(lambda g: calculate_new_location(g, empty_rows, empty_columns), galaxies)

    distances = map(lambda pair: manhatten_distance(*pair), combinations(expanded_galaxies, 2))

    print(sum(distances))
