from domador import Domador
from dragon import Dragon
from juego import Juego

dragon1 = Dragon(0, 30, "Flofi")
dragon2 = Dragon(10, 21, "Rufus")
dragon3 = Dragon(15, 12, "Nicolas Harari")
listaDragones = [dragon1, dragon2, dragon3]

domador1 = Domador(10, 15, "Pablo")
domador2 = Domador(20, 20, "Tania")
domador3 = Domador(30, 30, "Renata")
listaDomadores = [domador1, domador2, domador3]

juego = Juego(100, listaDragones, listaDomadores)

while not juego.estaTerminado():
    juego.avanzarTurno()
