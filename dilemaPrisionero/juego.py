class Juego:

    def __init__(self, matriz, jugador1, jugador2):
        self.__matriz = matriz
        self.__jugador1 = jugador1
        self.__jugador2 = jugador2
        self.__historia = []

    def correr (self, numerojugadas = 1):
        historiaParcial = []
        for i in range(numerojugadas):
            eleccion1 = self.__jugador1.estrategia()
            eleccion2 = self.__jugador2.estrategia()
            resultado = self.__matriz[eleccion1][eleccion2]
            historiaParcial.append(resultado)
        self.__historia.extend(historiaParcial)
        return historiaParcial

    def historia(self):
        return self.__historia

    def pagoEsperado(self):
        resultadoJugador1 = 0
        resultadoJugador2 = 0
        for value in self.__historia:
            resultadoJugador2 = resultadoJugador2 + value[1]
            resultadoJugador1 = resultadoJugador1 + value[0]
        return [resultadoJugador1/len(self.__historia), resultadoJugador2/len(self.__historia)]
