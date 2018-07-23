import random

class JugadorSimple:

    def __init__(self, p=0.5):
        self.ganasDeCooperar = p

    def decidir(self):
        return random.uniform(0,1) < self.ganasDeCooperar

    def guardarJugada(self, juego):
        pass
