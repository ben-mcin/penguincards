from deck import Deck
from player import Player
from card import Card, Element


ELEMENT_WINS_AGAINST = {
    Element.FIRE: Element.SNOW,
    Element.SNOW: Element.WATER,
    Element.WATER: Element.FIRE,
}


def determine_winner(card1: Card, card2: Card) -> str:
    if card1.element == card2.element:
        if card1.number == card2.number:
            return 0
        return 1 if card1.number > card2.number else 2

    return 1 if ELEMENT_WINS_AGAINST[card1.element] == card2.element else 2

# Initialise decks and players
player_deck = Deck()
computer_deck = Deck()

player = Player(player_deck)
computer = Player(computer_deck)

# Main game loop
while True:
    # Draw cards until both players have 5 cards in hand
    while len(player.get_hand()) < 5:
        player.draw_card()
    while len(computer.get_hand()) < 5:
        computer.draw_card()

    # Play cards
    player_card = player.play_card()
    computer_card = computer.play_card()

    print(f"Player plays: {player_card}\nComputer plays: {computer_card}")

    # Determine winning hand and add to players win conditions
    match determine_winner(player_card, computer_card):
        case 0:
            print("Draw")
        case 1:
            print("Player wins")
            player.add_win(player_card)
        case 2:
            print("Computer wins")
            computer.add_win(computer_card)

    break