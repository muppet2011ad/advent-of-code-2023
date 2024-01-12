from __future__ import annotations
from enum import Enum, auto
from collections import Counter
from functools import total_ordering

card_values = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

class HandType(Enum):
    K5 = auto()
    K4 = auto()
    FH = auto()
    K3 = auto()
    P2 = auto()
    P1 = auto()
    HC = auto()

hand_type_ordinal = {
    HandType.HC: 0,
    HandType.P1: 1,
    HandType.P2: 2,
    HandType.K3: 3,
    HandType.FH: 4,
    HandType.K4: 5,
    HandType.K5: 6
}

@total_ordering
class Hand:
    def __init__(self, cards: str, bid: int):
        self.bid = bid
        self.cards = cards
        self.values = list(map(card_values.get, cards))
        self.hand_type = self.get_hand_type(self.values)

    def __eq__(self, other: Hand) -> bool:
        return self.values == other.values
    
    def __lt__(self, other: Hand) -> bool:
        if self == other:
            return False
        if hand_type_ordinal[self.hand_type] < hand_type_ordinal[other.hand_type]:
            return True
        elif hand_type_ordinal[self.hand_type] > hand_type_ordinal[other.hand_type]:
            return False
        for cards in zip(self.values, other.values):
            if cards[0] < cards[1]:
                return True
            elif cards[0] > cards[1]:
                return False
            
    def __str__(self) -> str:
        return self.cards
        
    @staticmethod
    def get_hand_type(values: list[int]) -> HandType:
        counted_cards = Counter(values)
        common_cards = counted_cards.most_common()[:2]
        if len(common_cards) == 1:
            return HandType.K5
        pair1, pair2 = common_cards
        match pair1[1]:
            case 5:
                return HandType.K5
            case 4:
                return HandType.K4
            case 3:
                match pair2[1]:
                    case 1:
                        return HandType.K3
                    case 2:
                        return HandType.FH
            case 2:
                match pair2[1]:
                    case 1:
                        return HandType.P1
                    case 2:
                        return HandType.P2
            case 1:
                return HandType.HC

            

with open("D7/data") as f:
    hands_raw = f.readlines()
    hands = map(lambda x: Hand(x[0], int(x[1])), map(lambda x: x.split(), hands_raw))

    ranked_hands = sorted(hands)
    
    winnings = sum(map(lambda x: x[0] * x[1].bid, enumerate(ranked_hands, start=1)))

    print(winnings)
