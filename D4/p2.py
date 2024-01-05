import numpy as np

def parse_numbers(raw_numbers: str) -> set[int]:
    return set(map(int, raw_numbers.strip().split()))

def value_card(card: str) -> int:
    _, card_numbers = card.split(":")
    winning_numbers_raw, numbers_you_have_raw = card_numbers.split("|")
    winning_numbers = parse_numbers(winning_numbers_raw)
    numbers_you_have = parse_numbers(numbers_you_have_raw)

    matching_numbers = winning_numbers.intersection(numbers_you_have)

    return len(matching_numbers)

with open("D4/data") as f:
    cards = f.readlines()
    card_values = np.array(list(map(value_card, cards)), dtype=np.int32)
    num_cards = len(card_values)

    card_counts = np.ones(len(card_values), dtype=np.int32)
    current_card = 0

    while current_card < num_cards:
        card_value =  card_values[current_card]
        if card_value:
            card_counts[current_card + 1 : current_card + card_value + 1] += card_counts[current_card]
        current_card += 1

    print(card_counts.sum())
