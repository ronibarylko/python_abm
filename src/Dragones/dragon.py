import random

class Dragon:

    def __init__(self, posicionActual, edad, nombre):
        self.__estaDomado = False
        self.__edad = edad
        self.__posicionActual = posicionActual
        self.__nombre = nombre

    def obtenerPosicionActual(self):
        return self.__posicionActual

    def obtenerEdad(self):
        return self.__edad

    def estaDomado(self):
        return self.__estaDomado

    def obtenerNombre(self):
        return self.__nombre

    def capacidadDeAtaque(self, capacidad):
        return self.__edad * capacidad

    def mover(self, posicionMaxima):
        self.__posicionActual = (self.__posicionActual + 1 + random.randint(-3,3)) % posicionMaxima
        print "Le dragon " + self.__nombre + " se ha movido a la posicion " + str(self.__posicionActual)

    def cambiarEstado(self):
        self.__estaDomado = True
