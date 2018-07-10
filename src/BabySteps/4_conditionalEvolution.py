# coding=utf-8
import sys

def calculate(first_number, second_number, es_una_suma):
    result = 0
    if(es_una_suma == "suma"):
        result = int(first_number) + int(second_number)
    else:
        result = int(first_number) - int(second_number)
    return result

def sum_and_multiplicate_or_not(first_number, second_number, es_una_multiplicacion):
    result = calculate(first_number, second_number, "suma")
    if(es_una_multiplicacion == "multiplicacion"):
        if(result > 300):
            result = result*2
        else:
            result = result/2
        print("Mi resultado final es " + str(result))
    else:
        print("No hago nada a pedido tuyo")

sum_and_multiplicate_or_not(sys.argv[1], sys.argv[2], sys.argv[3])

''' Empieza a ponerse picante la cosa. Nuevas consideraciones: funciones que retornan parámetros, condicionales anidados.
Basicamente, dividimos nuestras responsabilidades en dos funciones. Y así podríamos hacerlo más veces, de ser necesario: una función que sume, una que multiplique,
otra que imprima en pantalla, una más que nos diga el mensaje que queremos imprimir. Las posibilidades son infinitas'''
