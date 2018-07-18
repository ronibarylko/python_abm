from dragon import Dragon
from domador import Domador

midragon = Dragon(3)
midragon.escupirFuego(3)
midomador = Domador(3)
midomador.domarDragon(midragon)
print(midragon.escupirFuego(midomador.obtenerCapacidad()))
