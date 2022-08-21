from card import Card
from deck_of_cards import Deck

STARTING_SCORE = 50
NUM_OF_GAMES = 7

while True:
    game_deck = Deck()  # Create a deck that will also create all cards
    game_deck.shuffle_deck()
    card = game_deck.pop_card()
    print(f"Starting card is: {card}")
    score = STARTING_SCORE
    for _ in range(NUM_OF_GAMES):
        new_card = game_deck.pop_card()
        response = ""
        while response != "h" and response != "l":
            response = input(
                f"Will the next be higher or lower than {card.rank} of {card.suit}, value: {card.value}? Type h or l: "
            )
        if (response == "h" and new_card.value > card.value) or (
            response == "l" and new_card.value < card.value
        ):
            print("You were right!")
            score += 20
        else:
            print("You lost")
            score -= 25
        print("\n")
        print(f"Card was {new_card.rank} of {new_card.suit}, value: {new_card.value}")
        if score <= 0:
            print(f"You have {score} points. You lost")
            break
        else:
            print(f"Your score is {score}" + "\n" + "-" * 30)

        card = new_card
    go_again = input("Would you like another round? y/n ")
    if go_again == "n":
        break
