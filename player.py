from deck import Deck
import random

class Player:
    def __init__(self, deck):
        self.player_deck = deck.cards.copy()
        random.shuffle(self.player_deck)
        self.hand = []
        self.graveyard = []
        self.wins = {"🔥" : set(),
                     "❄️" : set(),
                     "💧" : set()}

    # Shuffle player deck
    def shuffle_deck(self):
        random.shuffle(self.player_deck)

    # Draw card from deck, recycles graveyard if deck is empty, default draws 1 card
    def draw_card(self, count: int = 1):
        if not self.play_deck:
            self.recycle_graveyard()
        for x in range(0, count):
            self.hand.append(self.player_deck.pop(0))

    # Get cards in hand
    def get_hand(self):
        return self.hand

    def get_player_deck(self):
        return self.player_deck

    # Shuffle graveyard back into deck
    def recycle_graveyard(self):
        self.player_deck += self.graveyard
        self.graveyard = []
        self.shuffle_deck()
    
    # Select card from hand to play, defaults to a random card
    def play_card(self, int=random.randint(0,4)):
        card = self.hand.pop(int)
        self.graveyard.append(card)
        return card

    # Adds card to wins dictionary
    def add_win(self, card):
        self.wins[card.element.value].add(card.colour.value)

    def get_wins(self):
        return self.wins