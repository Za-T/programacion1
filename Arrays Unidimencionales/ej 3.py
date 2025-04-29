from biblioteca_funciones import *

def armar_lista_rango () -> list:

    lista_rango = [0] * 10

    for i in range (len(lista_rango)):
        lista_rango [i] = validar_int("un numero",1,100)

    return lista_rango

print (armar_lista_rango())