import re
from itertools import cycle
import math

parse_regex = re.compile(r"(\w\w\w) = \((\w\w\w), (\w\w\w)\)")

def network_step(network: dict[str, tuple[str, str]], current_node: str, instruction: str) -> str:
    options = network[current_node]
    match instruction:
        case "L":
            return options[0]
        case "R":
            return options[1]
        
# Checks if the last move in the list has previously appeared
# Returns length of cycle this implies if so, otherwise -1
def check_cycle_end(movelist: list[tuple[str, int]]) -> int:
    if not movelist[-1] in movelist[:-1]:
        return -1
    cycle_start = movelist[:-1].index(movelist[-1])
    return len(movelist) - cycle_start - 1

with open("D8/data") as f:
    lines = f.readlines()
    instructions = cycle(enumerate(lines[0].strip(" \n")))
    parsed_lines = map(lambda x: re.match(parse_regex, x).groups(), lines[2:])

    network = {str(x[0]): (str(x[1]), str(x[2])) for x in parsed_lines}
    current_nodes = list(filter(lambda x: x[-1] == "A", network.keys()))
    move_history = [[(start_node, lines[0][0])] for start_node in current_nodes]
    cycle_lengths = [-1] * len(current_nodes)
    steps = 0

    while not all(map(lambda c: c != -1, cycle_lengths)):
        seq, instruction = instructions.__next__()
        current_nodes = list(map(lambda node: network_step(network, node, instruction), current_nodes))
        print(current_nodes)
        for i, node in enumerate(current_nodes):
            move_history[i].append((node, seq))
            cycle_lengths[i] = check_cycle_end(move_history[i])
        steps += 1

    print(math.lcm(*cycle_lengths))