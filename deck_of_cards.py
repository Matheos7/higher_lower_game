from random import shuffle
from card import Card


class Deck:
    def __init__(self) -> None:
        SUIT_TUPLE = ("Spades", "Hearts", "Clubs", "Diamonds")
        RANK_TUPLE = (
            "Ace",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
        )
        self.cards = []
        for suit in SUIT_TUPLE:
            for value, rank in enumerate(RANK_TUPLE):
                # value + 1 because enum starts at index 0
                new_card = Card(rank, suit, value + 1)
                self.cards.append(new_card)

    def shuffle_deck(self):
        shuffle(self.cards)
        return self.cards

    def pop_card(self):
        popped_card = self.cards.pop()
        return popped_card

    def show(self):
        for card in self.cards:
            print(Card.show(card))

    def __repr__(self) -> str:
        return f"Deck of {len(self.cards)} cards"


# deck1 = Deck()
# deck1.shuffle_deck()
# print(deck1)
# print(deck1.pop_card())
# print(deck1)
# deck1.show()
