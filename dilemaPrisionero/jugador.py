import random

class Jugador:

    def __init__(self, probabilidad=0.5, memoria=1):
        self.__probabilidad = probabilidad
        self.__memoria = memoria

    def estrategia(self, matriz, decisiones):
        if len(decisiones) > self.__memoria:
            return self.tomarDecisionRacional(matriz, decisiones)
        else:
            return random.uniform(0,1) > self.__probabilidad

    def tomarDecisionRacional(self, matriz, decisiones):
        decisionesQueConsidero = decisiones[len(decisiones) - self.__memoria: len(decisiones) - 1]
        resultado=0
        for i in decisionesQueConsidero:
            resultado = resultado+i

        probCop = resultado/self.__memoria
        pagoEsperadoCoperar = probCop * (matriz[1][1][0] + matriz[1][0][0])
        pagoEsperadoNoCoperar = probCop * (matriz[0][1][0] + matriz[0][0][0])

        return pagoEsperadoCoperar > pagoEsperadoNoCoperar
