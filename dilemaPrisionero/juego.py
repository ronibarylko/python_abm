class Juego:

    def __init__(self, matriz, jugador1, jugador2):
        self.__matriz = matriz
        self.__jugador1 = jugador1
        self.__jugador2 = jugador2
        self.__historia = []
        self.__decisiones = []

    def correr (self, numerojugadas = 1):
        historiaParcial = []
        for i in range(numerojugadas):
            eleccion1 = self.__jugador1.estrategia(self.__matriz, self.decisionesDelOtroJugador(self.__jugador1))
            eleccion2 = self.__jugador2.estrategia(self.__matriz, self.decisionesDelOtroJugador(self.__jugador2))
            self.__decisiones.append([eleccion1, eleccion2])
            resultado = self.__matriz[eleccion1][eleccion2]
            historiaParcial.append(resultado)
        self.__historia.extend(historiaParcial)
        return historiaParcial

    def decisionesDelOtroJugador(self, jugador):
        decisionesJugador = []
        if jugador == self.__jugador1:
            for element in self.__decisiones:
                decisionesJugador.append(element[1])
        else:
            for element in self.__decisiones:
                decisionesJugador.append(element[0])
        return decisionesJugador

    def historia(self):
        return self.__historia

    def pagoEsperado(self):
        resultadoJugador1 = 0
        resultadoJugador2 = 0
        for value in self.__historia:
            resultadoJugador2 = resultadoJugador2 + value[1]
            resultadoJugador1 = resultadoJugador1 + value[0]
        return [resultadoJugador1/len(self.__historia), resultadoJugador2/len(self.__historia)]
