from player import Player
from copy import deepcopy
import random


def evaluate_win_condition(wins):
        element_win_score = sum(bool(items) for items in wins.values())
        fire_win_score = len(wins["🔥"])
        snow_win_score = len(wins["❄️"])
        water_win_score = len(wins["💧"])
        max_score = max(element_win_score, fire_win_score, snow_win_score, water_win_score)
        return max_score

def evaluate_card(card, wins):
    temp_wins = deepcopy(wins)
    temp_wins[card.element.value].add(card.colour.value)
    return evaluate_win_condition(temp_wins)


class CPU(Player):
    def __init__(self, deck, difficulty="dumb"):
        super().__init__(deck)

        self.difficulty = difficulty

        if difficulty == "normal":
            self.play_card = self._play_card_normal
        elif difficulty == "hard":
            self.play_card = self._play_card_hard
        elif difficulty == "dumb":
            pass
        else:
            raise ValueError("Invalid difficulty level. Choose from 'dumb', 'normal', or 'hard'.")

    # Implements normal difficulty where CPU makes decision based on it's own win conditions.
    def _play_card_normal(self, opponent_wins):
        # Gets weighting for each card in hand based on how it affects the CPU's win conditions
        scores = []
        for card in self.hand:
            score = evaluate_card(card, self.wins)
            scores.append((score, card))
        # Get the best score and the highest card number for that score
        best_score, best_number = max((score, card.number) for score, card in scores)

        result = random.choice([
            (score, card)
            for score, card in scores
            if (score, card.number) == (best_score, best_number)
        ])
        
        return super().play_card(self.hand.index(result[1]))

    # TODO implement smarter card selection for CPU
    def _play_card_hard(self, opponent_wins):
        # Play a random card from hand
        return super().play_card()