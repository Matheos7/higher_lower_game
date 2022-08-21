from numpy import RankWarning


class Card:
    def __init__(self, rank, suit, value) -> None:
        self.rank = rank
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.rank} of {self.suit}, value: {self.value}"

# card1 = Card("Ace", "Hearts", 1)
# print(card1.show())