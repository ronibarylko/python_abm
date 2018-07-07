import random
from itertools import izip

def mean(seq): #simplest computation of mean
    n = len(seq)
    return sum(seq)/float(n)

def transpose(seqseq): #simple 2-dimensional transpose
    return zip(*seqseq)

def random_pairs_of(players):
    """Return all of players as random pairs."""
    # copy player list
    players = list(players)
    # shuffle the new player list in place
    random.shuffle(players)
    # yield the shuffled players, 2 at a time
    player_iter = iter(players)
    return izip(player_iter, player_iter)

def topscore_playertypes(player):
    """Return list of best (maximum payoff) player types."""
    best_types = [player.playertype]
    best_payoff = player.get_payoff()
    for opponent in player.players_played:
        payoff = opponent.get_payoff()
        if payoff > best_payoff:
            best_payoff = payoff
            best_types = [opponent.playertype]
        elif payoff == best_payoff:
            best_types.append(opponent.playertype)
        return best_types
