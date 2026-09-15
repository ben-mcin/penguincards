from player import Player


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

    # TODO implement smarter card selection for CPU
    def _play_card_normal(self, self_wins, opponent_wins):
        # Play a random card from hand
        return super().play_card()

    # TODO implement smarter card selection for CPU
    def _play_card_hard(self, self_wins, opponent_wins):
        # Play a random card from hand
        return super().play_card()