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

    # Draw card from deck
    def draw_card(self):
        self.hand.append(self.player_deck.pop(0))

    # Get cards in hand
    def get_hand(self):
        return self.hand

    def get_player_deck(self):
        return self.player_deck

    #TODO recycle cards from graveyard into deck and shuffle
    def recycle_graveyard(self):
        return None
    
    #TODO allow player to select card from hand to play
    def play_card(self, card=None):
        card = self.hand.pop()
        self.graveyard.append(card)
        return card

