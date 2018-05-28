from utils import random_pairs_of
from cdiGame import CDIGame

class SoupRound:
    def __init__(self, players, payoffmat):
        self.players = players
        self.payoffmat = payoffmat

    def run(self):
        payoff_matrix = self.payoffmat
        for player1, player2 in random_pairs_of(self.players):
            game = CDIGame(player1, player2, payoff_matrix)
            game.run()
