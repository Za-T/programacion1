
def auxiliar_listas_dic (lista:list, clave:str, i:int,j:int):
    aux = lista [i] [clave]
    lista [i] [clave] = lista [j] [clave]
    lista [j] [clave] = aux

def promediar_notas (datos:list):

    #por cada elemento de la lista
    for i in range (len(datos)):

        suma_notas = 0

        #por cada nota
        for j in range (len(datos [i]["notas"])):
            suma_notas += datos[i]["notas"][j]

        cant_notas = len(datos [i]["notas"])

        promedio = suma_notas // cant_notas

        datos [i]["promedio"] = promedio

