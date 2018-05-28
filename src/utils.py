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
