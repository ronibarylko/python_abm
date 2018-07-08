# coding=utf-8
import sys

def calculate(first_number, second_number, es_una_suma):
    result = 0
    if(es_una_suma == "suma"):
        result = int(first_number) + int(second_number)
    else:
        result = int(first_number) - int(second_number)
    print("Mi resultado es " + str(result))

calculate(sys.argv[1], sys.argv[2], sys.argv[3])

'''Volvemos a utilizar parametros recibidos desde el llamado al programa. En este caso, surge una pregunta: que significa int()?
Basicamente, el sistema solo sabe recibir 'textos'. En términos de un programa, no es lo mismo tener un 3 como valor númerico, que un 3 en formato texto
Por esto es que debemos tomar el valor y convertirlo en un entero (integer ---> int). De este modo, somos capaces de calcular luego la suma

Ahora, cuando voy a imprimirlo en pantalla me encuentro con el caso contrario: quiero utilizar la función '+' para concatenar textos, pero uno de ellos
es un string (texto) y otro es un int (entero). No tengo más opcion que transformar el resultado nuevamente en un texto, para imprimirlo de la forma que deseo

Si quieren hacer la prueba, quiten la funcion int() y dejen el llamado resultado = first_number + second_number, y planteense que es lo que pasa
En caso de dudas, mail

Para los más despistados, dejo por aquí abajo una función un tanto más simple, que recibe parámetros internamente y, de este modo, no tiene que realizar ninguna conversión
Para utilizarla, sacarle el numeral al llamado (descomentarlo)'''

def calculate_only_numbers(first_number, second_number, es_una_suma):
    result = 0
    if(es_una_suma == "suma"):
        result = first_number + second_number
    else:
        result = first_number - second_number
    print(result)

#calculate_only_numbers(3, 2, "suma")
