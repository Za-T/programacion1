def ordenar_desc_lista_dic (lista:list,key:str)->list:

    for i in range (len(lista)-1):

        for j in range (i+1, len(lista)):

            if lista [i][key] >  lista [j][key]:

                aux = lista [i]
                lista [i] = lista [j]
                lista [j] = aux                

    return lista

def ordenar_asc_lista_dic (lista:list,key:str)->list:

    for i in range (len(lista)-1):

        for j in range (i+1, len(lista)):

            if lista [i][key] <  lista [j][key]:

                aux = lista [i]
                lista [i] = lista [j]
                lista [j] = aux                

    return lista

def promediar_item (lista_n: list, key: str) -> int:
    
    suma = 0
    cant_total = len(lista_n)

    for valor in lista_n:
        suma += valor [f"{key}"]
    
    promedio = suma / cant_total

    return promedio

def mostrar_lista_dic (lista:list):

    for i in range(len(lista)):

        diccionario = lista [i]

        for key, value in diccionario.items():
            print (f"{key}: {value}")
    
        print ("\n")

def filtrar_rango_dic (datos:list, key:str, minimo: float, maximo: float) -> list:

    lista = []

    for dicionario in datos:
        if (dicionario [f"{key}"] >= minimo) and (dicionario [f"{key}"] <= maximo):
            lista.append (dicionario)

    return lista

def mostrar_keys (datos:list,key_list:list):

    for i in range(len(datos)):
        for j in range (len(key_list)):
            print (f"{key_list[j]}: {datos[i][key_list[j]]}")
        print ("\n")

def auxiliar_listas_dic (lista:list, clave:str, i:int,j:int):
    aux = lista [i] [clave]
    lista [i] [clave] = lista [j] [clave]
    lista [j] [clave] = aux
