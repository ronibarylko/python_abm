# coding=utf-8
import sys

def reverseList(list_val):
    newList = list()
    for value in list_val:
        newList.insert(0, value)
    print(newList)

reverseList([3, 2, 1])

'''Imprimimos una lista y la damos vuelta. Vemos por primera vez la aparición de un For for comprehension, y la de listas.
En un for de este estilo, tenemos una iteración a través de una lista (o de cualquier cosa semejante que pueda ser
iterada) donde simplemente le decimos al programa como nombramos a la variable que estamos iterando. En este caso, usamos
"value", pero bien podriamos haberle puesto algo más descriptivo como "numeroDentroDeLista". Notar que, en estos casos la descriptividad
de las variables pasa desapercibida, pero cuando tengamos que enfrentarnos con estructuras más grandes cobrará importancia esta cuestión

Con respecto a las listas: en la computación del bien, se empieza contando desde el item 0. ¿Qué quiere decir esto? Si tengo tres elementos,
tengo las posiciones 0, 1 y 2 (notar que en nuestro programa colocamos los valores en la posición 0 de la nueva lista, es decir, la primera)
Se pueden hacer listas de cualquier cosa: de números, de palabras, de objetos creados por nosotros mismos, o listas de listas:

[1, 2, 3]
["hola", "chau", "mañana", ""]
[["a", "b", "c"], ["hola, "chau", "mañana"]]

¿Cuantos elementos hay en cada una de las tres listas de arriba?
Pueden investigar bien su estructura, y disfrutar de las distintas posibilidades que les brinda Python usando el infalible Google. "
