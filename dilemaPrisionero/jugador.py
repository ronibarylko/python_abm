import random

class Jugador:

    def __init__(self, probabilidad=0.5):
        self.__probabilidad = probabilidad

    def estrategia(self):
        return random.uniform(0,1) > self.__probabilidad
