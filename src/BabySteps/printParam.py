# coding=utf-8
import sys

def helloWorld(texto):
    print(texto)

helloWorld(sys.argv[1])

'''Usamos sys.argv porque es una convención de Python. El sistema recibe todos los parámetros y los introduce en un arreglo (en otros ejercicios veremos en profundidad esto)

 Otro ejemplo de uso de parámetros, esta vez a manopla (para correrlo sacarle el numeral): '''

#helloWorld("soy un bello texto")

''' Notar que en este caso, el usuario no elige el texto que se imprime: lo hace el programador.
A fin de cuentas, tenemos una función parametrizada, capaz de imprimir lo que nosotros querramos'''
