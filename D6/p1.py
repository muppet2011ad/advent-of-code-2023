import math

# c = (b - x)x where c is the distance, b is the total race time and x is the time the button is held down
# -x^2 + bx - c = 0 solving for x given a known b and c gives us the margin of error for that race
# and luckily I had to learn the quadratic formula for my GCSE :)

def solve_quadratic_real(a: float, b: float, c: float) -> list[float]:
    discriminant = pow(b, 2) - 4 * a * c
    if discriminant <= 0:
        return []
    elif discriminant == 0:
        return [-b/(2*a)]
    else:
        return sorted([(-b + math.sqrt(discriminant))/(2*a), (-b - math.sqrt(discriminant))/(2*a)])
    

def get_race_win_options(race: tuple[int, int]) -> int:
    solutions = solve_quadratic_real(-1, race[0], -(race[1] + 1)) # We want distance + 1 as we want to *beat* the record not match it
    match len(solutions):
        case 0:
            return 0
        case 1:
            return 1 if solutions[0].is_integer() else 0
        case 2:
            return math.floor(solutions[1]) - math.ceil(solutions[0]) + 1


with open("D6/data") as f:
    times_raw, distances_raw = f.readlines()
    times = map(int, times_raw.split(":")[1].strip().split())
    distances = map(int, distances_raw.split(":")[1].strip().split())

    races = zip(times, distances)
    
    win_options = list(map(get_race_win_options, races))
    print(win_options)

    print(math.prod(win_options))


