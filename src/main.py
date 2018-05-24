from randomMover import RandomMover
from simpleGame import SimpleGame
from randomPlayer import RandomPlayer
from simplePlayer import SimplePlayer
from cdiPlayerType import CDIPlayerType
from cdiGame import CDIGame

def main():
  print "Hello World!"


'''# PUNTO 3.8 ejercicio
# GAME: RandomMover
# create a payoff matrix and two players

PAYOFFMAT = [ [(3,3),(0,5)] , [(5,0),(1,1)] ] # Las 4 posibilidades del juego
player1 = RandomMover()
player2 = RandomMover()
# get a move from each player
move1 = player1.move()
move2 = player2.move()
# retrieve and print the payoffs
pay1, pay2 = PAYOFFMAT[move1][move2] # Dependiendo que hayan elegido, elijo el correspondiente en la matriz
print "Player1 payoff: ", pay1
print "Player2 payoff: ", pay2
print "Player1 payoff: ", move1
print "Player2 payoff: ", move2'''


'''# PUNTO 3.23 ejercicio
# GAME: SimpleGame with RandomPlayer
# create a payoff matrix and two players
PAYOFFMAT = [ [(3,3),(0,5)] , [(5,0),(1,1)] ]
player1 = RandomPlayer(p=0.6)
player2 = RandomPlayer(p=0.0)
# create and run the game
game = SimpleGame(player1, player2, PAYOFFMAT)
game.run()
# retrieve and print the payoffs
payoffs = game.payoff()
print "Player1 payoff: ", payoffs[player1]
print "Player2 payoff: ", payoffs[player2]'''

# PUNTO 4.16 ejercicio
## GAME: CDIGame with SimplePlayer
# create a payoff matrix and two players (with playertypes)
PAYOFFMAT = [ [(3,3),(0,5)] , [(5,0),(1,1)] ]
ptype1 = CDIPlayerType()
ptype2 = CDIPlayerType()
player1 = SimplePlayer(ptype1)
player2 = SimplePlayer(ptype2)
# create and run the game
game = CDIGame(player1, player2, PAYOFFMAT)
game.run()
# retrieve and print the payoffs
payoffs = game.payoff()
print "Player1 payoff: ", payoffs[player1]
print "Player2 payoff: ", payoffs[player2]
