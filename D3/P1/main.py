from functools import reduce

class Coord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    neighbours = lambda self:  [Coord(self.x - 1, self.y), Coord(self.x + 1, self.y),
                                Coord(self.x - 1, self.y - 1), Coord(self.x, self.y - 1), Coord(self.x + 1, self.y - 1), 
                                Coord(self.x - 1, self.y + 1), Coord(self.x, self.y + 1), Coord(self.x + 1, self.y + 1)]
    
    def __eq__(self, __value: object) -> bool:
        return type(__value) is Coord and self.x == __value.x and self.y == __value.y
        

class Number:
    def __init__(self, value: int, coords: list[Coord],):
        neighbours = reduce(lambda x, y: x+y, map(lambda x: x.neighbours(), coords), [])
        self.neighbours = []
        [self.neighbours.append(x) for x in neighbours if x not in self.neighbours]
        self.value = value

    def is_part_number(self, symbol_coords: list[Coord]):
        return any(map(lambda x: x in self.neighbours, symbol_coords))
    

class Parser:
    def __init__(self,  schematic):
        self.loc = [0, 0]
        self.num_value_buffer = ""
        self.num_coord_buffer = []
        self.numbers = []
        self.symbols_coords = []
        self.schematic = schematic

    def finish_number(self):
        if not self.is_in_number():
            return
        self.numbers.append(Number(int(self.num_value_buffer), self.num_coord_buffer))
        self.num_value_buffer = ""
        self.num_coord_buffer = []

    def is_in_number(self):
        return self.num_value_buffer != ""

    def parse_schematic(self) -> tuple[list[Number], list[Coord]]:
        c = self.schematic.read(1)
        while c:
            if c == "\n":
                self.loc[0] = 0
                self.loc[1] += 1
                self.finish_number()
                c = self.schematic.read(1)
                continue
            elif c == ".":
                self.finish_number()
            elif c.isdigit():
                self.num_value_buffer = self.num_value_buffer + c
                self.num_coord_buffer.append(Coord(*self.loc))
            else:
                self.finish_number()
                self.symbols_coords.append(Coord(*self.loc))
            self.loc[0] += 1
            c = self.schematic.read(1)
        return self.numbers, self.symbols_coords


with open("D3/data") as f:
    parser = Parser(f)
    numbers, symbols = parser.parse_schematic()
    part_numbers = filter(lambda x: x.is_part_number(symbols), numbers)
    part_numbers_sum = sum(map(lambda x: x.value, part_numbers))

    print(part_numbers_sum)

