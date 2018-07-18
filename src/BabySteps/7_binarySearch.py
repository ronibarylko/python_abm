# coding=utf-8
import sys

def binarySearch(numberList, number):
    positionLeft = 0
    positionRight = len(numberList)
    findValue = False

    if numberList[0] == number:
        print("El valor " + str(number) + " se encuentra en la posición 0")
        findValue = True #Este if me salva del caso base, en que el valor esta en la primer posición (la única que no chequeo). No le den tanta bola

    while (not findValue) and (positionRight > positionLeft+1):
        middleValue = (positionLeft + positionRight)/2
        if(numberList[middleValue] > number):
            positionRight = middleValue
        else:
            if(numberList[middleValue] < number):
                positionLeft = middleValue
            else:
                findValue = True
                print("El valor " + str(number) + " se encuentra en la posición " + str(middleValue))
    if not findValue:
        print("No se encontró el valor " + str(number) + " en la lista")


binarySearch([1, 2, 3, 4, 5], 3)

'''IMPORTANTE: Si no sabes que hace una búsqueda binaria, no esperes entender qué es lo que pasa. Mandá mail o googleá, después de entender la idea se facilita
mucho entender el código. Como ayuda memoria, básicamente nos pasan una lista ORDENADA de menor a mayor, y un valor numérico, y nosotros debemos buscar en qué posición
se encuentra este número de la forma más rapida posible

Antes de entrar en el análisis del ejercicio, veamos que aparecen varias novedades, entre las cuales destacan los booleanos y los signos de negación, and y or.

Los booleanos son, básicamente, los valores de verdad: VERDADERO o FALSO. Hay teoria copada detrás de ellos, pero no vamos a detenernos en eso.
En este caso, usamos un booleano para definir si ya encontramos el número que buscamos o no, y para definir si queremos seguir iterando en nuestro ciclo

Los signos de negación, and y or son muy bellos en Python, ya que se limitan al uso de las propias palabras NOT, AND y OR. En lenguajes menos bellos tendríamos
!, && y ||, asi que agradezcan a quien haya creado tan legible lenguaje.

La idea del ejercicio es tan simple como bella. Dado que nuestra lista está ordenada, sabemos que al pararnos en un valor cualquiera de la lista, todos a la izquierda
son menores, y todos a la derecha mayores. Por lo tanto, si partimos la lista en dos cada vez que avanzamos una iteración de ciclo, y comparamos el valor del medio con
el que estamos buscando, podemos definir si los que tenemos que descartar son los de la mitad izquierda o de la mitad derecha. Así, en vez de recorrer todos los valores
de la lista para saber si el numero buscado se encuentra, partimos constantemente la lista en 2 y reducimos notablemente el tiempo consumido

Por ejemplo, para una lista de 8 elementos, deberíamos partirlo primero en dos mitades de 4, luego en dos mitades de 2, y luego en dos mitades de 1. Es decir, en el peor caso
usamos 4 pasos en lugar de 8.
Para una lista de 32, tendríamos : 32 -> 16 -> 8 -> 4 -> 2 -> 1. Seis pasos para definir si un valor se encuentra en esos 32 numeros! Imaginenlo con valores mucho más grandes:
listas de millones de números, reducidos constantemente a mitades y mitades y mitades.

 '''
