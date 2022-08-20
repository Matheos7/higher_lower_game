from random import shuffle
from copy import copy

NUM_OF_GAMES = 7
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


def shuffle_deck(deck: list) -> list:
    """
    Takes new deck of cards and returns shuffled copy of it
    """
    shuffled_deck = copy(deck)
    shuffle(shuffled_deck)
    return shuffled_deck


def get_card(deck: list) -> dict:
    """
    Takes shuffled deck of cards and returns one card represented as dict
    """
    card = deck.pop()
    return card


print("Welcome to the higher lower game")

# Create a deck of cards
deck_of_cards = []
for suit in SUIT_TUPLE:
    for value, rank in enumerate(RANK_TUPLE):
        new_card = {"rank": rank, "suit": suit, "value": value + 1}
        deck_of_cards.append(new_card)

while True:  # Main loop of the game that reverts back here if 'go again' at the bottom is 'y', else breaks out and ends
    # Prepare a game deck that is shuffled and then pop a card that will be presented at the beginning of the game 
    score = 50
    game_deck = shuffle_deck(deck_of_cards)
    card = get_card(game_deck)
    print(f"This is the starting card: {card['rank']} of {card['suit']}, value: {card['value']}")
    print("\n\n")

    for _ in range(NUM_OF_GAMES): # Loops for the amount of guesses in one game
        response = input(f"Will the next be higher or lower than {card['rank']} of {card['suit']}, value: {card['value']}? Type h or l: ")
        print("\n")
        new_card = get_card(game_deck)  # Get another card to compare to previous one
        
        if response != "h" and response != "l":
            print("You need to type in either h or l")

        elif (response == "h" and new_card["value"] > card["value"]) or (
            response == "l" and new_card["value"] < card["value"]
        ):
            print("You were right!")
            score += 20

        else:
            print("You lost")
            score -= 25

        print(
            f"Card was {new_card['rank']} of {new_card['suit']}, value: {new_card['value']}"
        )
        if score <= 0:
            print("You don't have enough points to keep playing. You lost")
            break
        else:    
            print(f"Your score is {score}" + "\n\n" + '-' * 30)

        card = new_card
    go_again = input("Would you like another round? y/n")
    if go_again == "n":
        break
