from biblioteca_funciones import *


def armar_lista_numeros ()->list:

    '''Le pide al usuario la posicion en la lista y el valor a guardar,"
    permite armar una lista de maximo 10 valores.'''

    lista_numeros = [0] * 10

    respuesta = "s"
     
    while respuesta == "s":

        posicion = validar_int ("posicion", 0, 9)

        numero = solicitar_entero ("numero")

        lista_numeros [posicion] = numero

        respuesta = validar_str ("si quiere insertar otro numero", "s", "n")

    return [lista_numeros]
        

print (armar_lista_numeros())