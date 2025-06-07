from biblioteca_funciones import *

def promediar_notas (datos:list):

    key_list = ["legajo","nombre", "apellido", "promedio"]

    #por cada elemento de la lista
    for i in range (len(datos)):

        suma_notas = 0

        #por cada nota
        for j in range (len(datos [i]["notas"])):
            suma_notas += datos[i]["notas"][j]

        cant_notas = len(datos [i]["notas"])

        promedio = suma_notas // cant_notas

        datos [i]["promedio"] = promedio

    mostrar_keys (datos, key_list)

        

