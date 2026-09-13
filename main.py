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
            return "draw"
        return "player" if card1.number > card2.number else "cpu"

    return "player" if ELEMENT_WINS_AGAINST[card1.element] == card2.element else "cpu"


player_deck = Deck()
computer_deck = Deck()

player = Player(player_deck)
computer = Player(computer_deck)

# Initial setup
player.draw_card()
player.draw_card()
player.draw_card()
player.draw_card()
player.draw_card()

computer.draw_card()
computer.draw_card()
computer.draw_card()
computer.draw_card()
computer.draw_card()

player_card = player.play_card()
computer_card = computer.play_card()
print(f"{player_card} vs {computer_card}")

print(f"{determine_winner(player_card, computer_card)} wins")