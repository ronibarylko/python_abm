from utils import mean,transpose

class JuegoSimple:

    def __init__(self, jugador1, jugador2, matrizDeDecisiones):
        self.jugadores = [jugador1, jugador2]
        self.matrizDeDecisiones = matrizDeDecisiones
        self.historia = list()

    def correr(self, iteraciones=4):
        jugador1, jugador2 = self.jugadores
        # Para cada iteracion, hace un nuevo movimiento y lo agrega a la historia
        for iteracion in range(iteraciones):
            nuevoMovimiento = jugador1.decidir(), jugador2.decidir()
            self.historia.append(nuevoMovimiento)
        # prompt players to record the game played (i.e., 'self')
        jugador1.guardarJugada(self)
        jugador2.guardarJugada(self)

    def condena(self):
        jugador1, jugador2 = self.jugadores
        # generate a payoff pair for each game iteration
        condenas = (self.matrizDeDecisiones[m1][m2] for (m1,m2) in self.historia)
        # Transponemos la matriz para obtener una secuencia por jugador
        condenas1, condenas2 = transpose(condenas)
        print(pay1)
        print(pay2)
        # return a mapping of each player to its mean payoff
        return { jugador1:mean(pay1), jugador2:mean(pay2) }
