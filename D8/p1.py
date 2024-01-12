import re
from itertools import cycle

parse_regex = re.compile(r"(\w\w\w) = \((\w\w\w), (\w\w\w)\)")

with open("D8/data") as f:
    lines = f.readlines()
    instructions = cycle(lines[0].strip(" \n"))
    parsed_lines = map(lambda x: re.match(parse_regex, x).groups(), lines[2:])

    network = {str(x[0]): (str(x[1]), str(x[2])) for x in parsed_lines}
    current_node = "AAA"
    steps = 0

    while current_node != "ZZZ":
        options = network[current_node]
        match instructions.__next__():
            case "L":
                current_node = options[0]
            case "R":
                current_node = options[1]
        steps += 1

    print(steps)