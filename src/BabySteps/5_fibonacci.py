# coding=utf-8
import sys

def fibonacci_while(quantity):
    iterator = 0
    fibonacci_n1 = 1
    fibonacci_n2 = 1
    while(iterator < quantity):
        aux = fibonacci_n1
        fibonacci_n1 = fibonacci_n2
        fibonacci_n2 = fibonacci_n1 + aux
        iterator += 1
    return fibonacci_n2

def fibonacci_recursive(quantity):
    return fibonacci_recursive_aux(quantity, 1 ,1)

def fibonacci_recursive_aux(quantity, fib_1, fib_2):
    if(quantity == 0):
        return fib_2
    else:
        return fibonacci_recursive_aux(quantity - 1, fib_2, fib_1 + fib_2)

print("While me devuelve " + str(fibonacci_while(int(sys.argv[1]))))
print("Recursividad me devuelve " + str(fibonacci_recursive(int(sys.argv[1]))))

'''Surgen dos nuevos conceptos: el uso de while (mientras que) y la recursividad. Dos funcionalidades distintas para un mismo problema: repetir una ejecución hasta
que un condicional la detenga

WHILE: Mientras que (condicion esperada) no ocurra, se sigue ejecutando el bloque de código. Notar la importancia de que la condición tenga un final, pues sino podríamos
quedarnos ejecutando eternamente (en este caso, si no avanzaramos el iterador).

RECURSIVIDAD: Se llama una función repetidas veces, de manera que se tengan dos casos: el caso base, con el que la ejecución acaba, y el caso intermedio, que hace un procesamiento
y continua con un nuevo llamado recursivo'''
