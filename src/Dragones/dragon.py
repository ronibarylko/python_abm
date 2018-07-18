class Dragon:

    def __init__(self, edad):
        self.__edad = edad
        self.__domado = False

    def escupirFuego(self, capacidadDomador):
        if self.__domado:
            return self.__edad * capacidadDomador
        else:
            print("Los dragones no domados no saben escupir fuego")
            return 0

    def domar(self):
        self.__domado = True

    def estaDomado(self):
        return self.__domado

    def volar(self):
        #Movimiento random
        return 0
