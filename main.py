from deck import Deck
from player import Player
from card import Card, Element


# Win conditions for card elements
ELEMENT_WINS_AGAINST = {
    Element.FIRE: Element.SNOW,
    Element.SNOW: Element.WATER,
    Element.WATER: Element.FIRE,
}


# Determine winning hand
def determine_hand_winner(card1: Card, card2: Card) -> str:
    if card1.element == card2.element:
        if card1.number == card2.number:
            return 0
        return 1 if card1.number > card2.number else 2

    return 1 if ELEMENT_WINS_AGAINST[card1.element] == card2.element else 2

# Check if a player meets win conditions
def check_win_condition(player: Player) -> bool:
    if all(player.get_wins().values()) or any(len(colours) == 3 for colours in player.get_wins().values()):
        return True

# Gets a player to choose a card from their hand
def choose_card(hand: list[Card]) -> Card:
    for i, option in enumerate(hand, 1):
        print(f"{i}: {option}")

    while True:
        try:
            return int(input("Choose a card: ")) - 1
        except (ValueError, IndexError):
            print("Invalid choice.")


# Initialise decks and players
player_deck = Deck()
cpu_deck = Deck()

player = Player(player_deck)
cpu = Player(cpu_deck)

# Main game loop
while True:
    # Draw cards until both players have 5 cards in hand
    while len(player.get_hand()) < 5:
        player.draw_card()
    while len(cpu.get_hand()) < 5:
        cpu.draw_card()

    # Play cards
    player_card = player.play_card(choose_card(player.get_hand()))
    cpu_card = cpu.play_card()

    print(f"Player plays: {player_card}\nCPU plays: {cpu_card}")

    # Determine winning hand and add to players win conditions
    match determine_hand_winner(player_card, cpu_card):
        case 0:
            print("Draw")
        case 1:
            print("Player wins")
            player.add_win(player_card)
        case 2:
            print("CPU wins")
            cpu.add_win(cpu_card)
    

    print(f"\nPlayer wins: {player.get_wins()}\nCPU wins: {cpu.get_wins()}")

    # Check if win conditions have been met
    if check_win_condition(player):
        print(f"\nPlayer has won the game with the following:\n{player.get_wins()}")
        break
    if check_win_condition(cpu):
        print(f"\nCPU has won the game with the following:\n{cpu.get_wins()}")
        break