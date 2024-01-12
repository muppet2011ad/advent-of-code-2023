from itertools import batched, chain # Batched requires Python 3.12 to run

class Map:
    def __init__(self, ranges: list[tuple[int, int, int]]):
        self.ranges = ranges

    def __call__(self, x: int) -> int:
        for candidate_range in self.ranges:
            if self.is_in_range(x, candidate_range):
                return self.apply_range(x, candidate_range)
        return x

    @staticmethod
    def is_in_range(x: int, range_to_check: tuple[int, int, int]) -> bool:
        return x in range(range_to_check[1], range_to_check[1] + range_to_check[2])
    
    @staticmethod
    def apply_range(x: int, range_to_apply: tuple[int, int, int]) -> int:
        return range_to_apply[0] + x - range_to_apply[1]

def apply_maps(maps: list[Map], x) -> int:
    for map in maps:
        x = map(x)
    return x

with open("D5/data") as f:
    lines = f.readlines()

    raw_seed_ranges = map(int, lines[0].split(":")[1].strip().split())
    seed_ranges = []
    for seed_range in batched(raw_seed_ranges, 2):
        seed_ranges.append(range(seed_range[0], seed_range[0] + seed_range[1]))
    seeds = chain(*seed_ranges)

    maps = []
    ranges = []
    for line in lines[3:]:
        if not line.strip():
            continue
        if "map" in line:
            maps.append(Map(ranges))
            ranges = []
        else:
            ranges.append(tuple(map(int, line.split())))
    if ranges:
        maps.append(Map(ranges))
    
    lowest_location = min(map(lambda x: apply_maps(maps, x), seeds))
    print(lowest_location)
