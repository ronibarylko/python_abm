import random

class RandomMover:
    def move(self):
        return random.uniform(0,1) < 0.5
