import random

class Jugador:

    def __init__(self, probabilidad=0.5, memoria=1):
        self.__probabilidad = probabilidad
        self.__memoria = memoria

    def estrategia(self, matriz, decisiones):
        if len(decisiones) > self.__memoria:
            tomarDecisionRacional(matriz, decisiones)
        else:
            return random.uniform(0,1) > self.__probabilidad

    def tomarDecisionRacional(self, matriz, decisiones):
        decisionesQueConsidero = decisiones[len(decisiones) - self.__memoria: len(decisiones) - 1]
        resultado=0
        for i in decisionesQueConsidero:
            resultado = resultado+i

        probCop = resultado/self.__memoria
        pagoEsperadoCoperar = probCop * (matrizDePagos [1][1][0] + matrizDePagos [1][0][0])
        pagoEsperadoNoCoperar = probCop * (matrizDePagos [0][1][0] + matrizDePagos [0][0][0])

        return pagoEsperadoCoperar > pagoEsperadoNoCoperar



        -veo las ultimas K del rival  (0,1)----> cada jugada vale 1/(cantidad de jugadas que se ven)
                    (supongamos 4 C + 1 NC)
        -tengo C/5 * pagoC|C + NC/5 * pago C|NC == pago cooperar
        -tengo C/5 * pagoNC|C + NC/5 * pago NC|NC == pago no cooperar
