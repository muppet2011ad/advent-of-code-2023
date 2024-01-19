from typing import Literal
from collections import deque

# Coords correspond to array indexing, so the northwest corner is at (0, 0), and the southeast corner at (n, n)
type Coords = tuple[int, int]

type Direction = Literal["n", "s", "e", "w"]

type Tile = Literal["|", "-", "L", "J", "7", "F", ".", "S"]

type Map = list[list[Tile]]

def find_S(map: Map) -> Coords:
    for x, line in enumerate(map):
        if "S" in line:
            return (x, line.index("S"))

def get_tile(map: Map, coords: Coords) -> Tile:
    return map[coords[0]][coords[1]]

def get_connecting_directions(tile: Tile) -> tuple[Direction, Direction] | None:
    match tile:
        case "|":
            return ("n", "s")
        case "-":
            return ("e", "w")
        case "L":
            return ("n", "e")
        case "J":
            return ("n", "w")
        case "7":
            return ("s", "w")
        case "F":
            return ("s", "e")
        case _:
            return None

def step(coords: Coords, direction: Direction) -> Coords:
    match direction:
        case "n":
            return (coords[0] - 1, coords[1])
        case "s":
            return (coords[0] + 1, coords[1])
        case "e":
            return (coords[0], coords[1] + 1)
        case "w":
            return (coords[0], coords[1] - 1)
        
        
with open("D10/data") as f:
    pipe_map: list[list[Tile]] = list(map(list, f.readlines()))

    start = find_S(pipe_map)
    explored: list[tuple[Coords, int]] = [] # list of explored coords and their distance from start
    queue: deque[tuple[Coords, int]] = deque([(start, 0)]) # Queue to be explored

    explored_coords = lambda: map(lambda x: x[0], explored)

    # we basically want a bfs

    while queue:
        current: tuple[Coords, int] = queue.popleft()
        if current[0] not in explored_coords():
            tile = get_tile(pipe_map, current[0])
            if tile == "S":
                successors = []
                north, south, east, west = step(current[0], "n"), step(current[0], "s"), step(current[0], "e"), step(current[0], "w")
                if get_tile(pipe_map, north) in ["|", "7", "F"]:
                    successors.append(north)
                if get_tile(pipe_map, south) in ["|", "L", "J"]:
                    successors.append(south)
                if get_tile(pipe_map, east) in ["-", "7", "J"]:
                    successors.append(east)
                if get_tile(pipe_map, west) in ["-", "L", "F"]:
                    successors.append(west)
            else:
                connecting_directions = get_connecting_directions(tile)
                candidate_successors = list(map(lambda d: step(current[0], d), connecting_directions))
                successors = list(filter(lambda x: x != current[0] and x not in explored_coords(), candidate_successors))

            to_enqueue = map(lambda x: (x, current[1] + 1), successors)
            queue.extend(to_enqueue)

            explored.append(current)

    max_distance = max(map(lambda x: x[1], explored))

    print(max_distance)

