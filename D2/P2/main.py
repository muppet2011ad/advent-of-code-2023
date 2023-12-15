validity = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open("D2/P2/data") as f:
    games = f.readlines()
    valid_games = []
    total_power = 0
    for game in games:
        game_number_str, game_text = game.split(":")
        game_number_int = int(game_number_str.split()[1])
        rounds = [x.strip() for x in game_text.split(";")]
        colour_max_occurrences = {}
        for round in rounds:
            draws = [x.strip() for x in round.split(",")]
            for draw in draws:
                count_str, colour = draw.split()
                count = int(count_str)
                if colour not in colour_max_occurrences or colour_max_occurrences[colour] < count:
                    colour_max_occurrences[colour] = count
        game_is_valid = True
        power = 1
        for colour in colour_max_occurrences:
            power *= colour_max_occurrences[colour]
            if colour_max_occurrences[colour] > validity[colour]:
                game_is_valid = False
        if game_is_valid:
            valid_games.append(game_number_int)
        total_power += power
    
    print(f"Valid game sum: {sum(valid_games)}\nPower sum: {total_power}")
                
