import random

class Domador:

    def __init__(self, posicionActual, capacidad, nombre):
        self.__posicionActual = posicionActual
        self.__capacidad = capacidad
        self.__listaDragones = []
        self.__nombre = nombre

    def obtenerPosicionActual(self):
        return self.__posicionActual

    def obtenerListaDragones(self):
        return self.__listaDragones

    def obtenerCapacidad(self):
        return self.__capacidad

    def obtenerNombre(self):
        return self.__nombre

    def mover(self, posicionMaxima):
        self.__posicionActual = (self.__posicionActual + random.randint(-1, 1)) % posicionMaxima
        print "Le domadorx " + self.__nombre + " se ha movido a la posicion " + str(self.__posicionActual)

    def cazarDragon(self, dragon):
        if not dragon.estaDomado():
            print "Le domadorx " + self.obtenerNombre() + " ha cazado al dragon " + dragon.obtenerNombre()
            self.__listaDragones.append(dragon)
            dragon.cambiarEstado()

    def capacidadTotal(self):
        resultado = 0
        for dragon in self.__listaDragones:
            resultado = resultado + dragon.capacidadDeAtaque(self.__capacidad)
        return resultado
