class Juego:

    def __init__(self, posicionMaxima, listaDragones, listaDomadores):
        self.__posicionMaxima = posicionMaxima
        self.__listaDragones = listaDragones
        self.__listaDomadores = listaDomadores
        self.__cantidadTurnos = 0
        self.__juegoTerminado = False

    def avanzarTurno(self):
        if self.__juegoTerminado:
            print "No se puede avanzar dado que el juego ha terminado"
        else:
            print "--"
            self.moverDragonesYDomadores()
            self.__cantidadTurnos = self.__cantidadTurnos + 1

    def moverDragonesYDomadores(self):
        for dragon in self.__listaDragones:
            dragon.mover(self.__posicionMaxima)

        for domador in self.__listaDomadores:
            domador.mover(self.__posicionMaxima)
            for dragon in self.__listaDragones:
                if domador.obtenerPosicionActual() == dragon.obtenerPosicionActual():
                    domador.cazarDragon(dragon)

        self.__juegoTerminado = self.chequearSiTerminoElJuego()

    def chequearSiTerminoElJuego(self):
        for dragon in self.__listaDragones:
            if not dragon.estaDomado():
                print "Fin del turno " + str(self.__cantidadTurnos) + "\n \n \n"
                return False
        print "\n \n \n El juego ha terminado. Lx ganadorx es " + self.definirGanador()
        return True

    def definirGanador(self):
        maxValor = 0
        ganador = ""
        for domador in self.__listaDomadores:
            if domador.capacidadTotal() > maxValor:
                maxValor = domador.capacidadTotal()
                ganador = domador.obtenerNombre()
        return ganador

    def estaTerminado(self):
        return self.__juegoTerminado
