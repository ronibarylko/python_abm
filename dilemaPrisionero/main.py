import random
from jugador import Jugador

#Matriz de pagos
fila1 = [[3,3], [0,10]]
fila2 = [[10,0], [6,6]]
matrizDePagos = [fila1, fila2]

# Dilema del prisionero simple
'''jugador1 = random.randint(0,1)
jugador2 = random.randint(0,1)

resultado = matrizDePagos[jugador1][jugador2]
print "El jugador 1 recibio " + str(resultado[0])
print "El jugador 2 recibio " + str(resultado[1])'''

# Dilema del prisionero con probabilidad

jugador1 = Jugador(1)
jugador2 = Jugador(0)

eleccion1 = jugador1.estrategia()
eleccion2 = jugador2.estrategia()

resultado = matrizDePagos[eleccion1][eleccion2]
print "El jugador 1 recibio " + str(resultado[0])
print "El jugador 2 recibio " + str(resultado[1])
