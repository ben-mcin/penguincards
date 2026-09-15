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

def evaluate_opponent(wins):
    scores = {"element_win": sum(bool(items) for items in wins.values()),
              "🔥": len(wins["🔥"]),
              "❄️": len(wins["❄️"]),
              "💧": len(wins["💧"])}
    return scores


AVOID_ELEMENTS = {
    "🔥": "❄️",
    "❄️": "💧",
    "💧": "🔥",
}


class CPU(Player):
    def __init__(self, deck, difficulty="dumb"):
        super().__init__(deck)

        self.difficulty = difficulty

        if difficulty == "easy":
            self.play_card = self._play_card_easy
        elif difficulty == "normal":
            self.play_card = self._play_card_normal
        elif difficulty == "dumb":
            pass
        else:
            raise ValueError("Invalid difficulty level. Choose from 'dumb', 'normal', or 'hard'.")

    # Implements normal difficulty where CPU makes decision based on it's own win conditions.
    def _play_card_easy(self, opponent_wins):
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

    # Implements normal difficulty where CPU plays based on opponents win conditions, falling back on easy difficulty if none available
    def _play_card_normal(self, opponent_wins):
        likely_choices = set()
        weighted_choices = evaluate_opponent(opponent_wins)
        if weighted_choices.get("element_win") == max(v for k, v in weighted_choices.items()):
            for k, v in weighted_choices.items():
                if v == 0 and k != "element_win":
                    likely_choices.add(k)
        for k, v in weighted_choices.items():
            if k != "element_win" and v == max(v for k, v in weighted_choices.items()):
                if k != "element_win":
                    likely_choices.add(k)
        avoid = {AVOID_ELEMENTS[x] for x in likely_choices}

        scores = []
        for card in self.hand:
            if card.element.value in avoid:
                print(f"avoiding {card}")
                pass
            else:
                score = evaluate_card(card, self.wins)
                scores.append((score, card))

        if len(scores) > 0:
            best_score, best_number = max((score, card.number) for score, card in scores)
            result = random.choice([
                        (score, card)
                        for score, card in scores
                        if (score, card.number) == (best_score, best_number)
                    ])
            return super().play_card(self.hand.index(result[1]))
        else:
            print("no defensive choice")
            return self._play_card_easy(opponent_wins)

    # Implements hard difficulty where CPU randomises play between opponents win conditions and it's own
    def _play_card_hard(self, opponent_wins):
        if random.random() < 0.5:
            self._play_card_easy(opponent_wins)
        else:
            self._play_card_normal(opponent_wins)
    