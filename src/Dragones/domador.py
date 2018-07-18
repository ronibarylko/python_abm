class Domador:

    def __init__(self, capacidad):
        self.__capacidad = capacidad
        self.__dragonesDomados = []

    def domarDragon(self, dragon):
        if not dragon.estaDomado():
            dragon.domar()

    def obtenerCapacidad(self):
        return self.__capacidad
