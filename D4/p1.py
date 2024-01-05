def parse_numbers(raw_numbers: str) -> set[int]:
    return set(map(int, raw_numbers.strip().split()))

def value_card(card: str) -> int:
    _, card_numbers = card.split(":")
    winning_numbers_raw, numbers_you_have_raw = card_numbers.split("|")
    winning_numbers = parse_numbers(winning_numbers_raw)
    numbers_you_have = parse_numbers(numbers_you_have_raw)

    matching_numbers = winning_numbers.intersection(numbers_you_have)

    return 0 if not matching_numbers else pow(2, len(matching_numbers) - 1)

with open("D4/data") as f:
    cards = f.readlines()
    total = sum(map(value_card, cards))
    print(total)