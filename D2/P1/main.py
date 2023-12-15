validity = {
    "red": 12,
    "green": 13,
    "blue": 14
}

with open("D2/P1/data") as f:
    games = f.readlines()
    valid_games = []
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
        for colour in colour_max_occurrences:
            if colour_max_occurrences[colour] > validity[colour]:
                game_is_valid = False
        if game_is_valid:
            valid_games.append(game_number_int)
    
    print(sum(valid_games))
                
