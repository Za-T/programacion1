peliculas = [ 
{"titulo": "Inception", "anio": 2010, "puntaje": 8.8}, 
{"titulo": "The Matrix", "anio": 1999, "puntaje": 8.7}, 
{"titulo": "Interstellar", "anio": 2014, "puntaje": 8.6}, 
{"titulo": "Avatar", "anio": 2009, "puntaje": 7.8}, 
{"titulo": "The Batman", "anio": 2022, "puntaje": 7.9} 
] 

def ordenar_asc_lista_dic (lista:list,key:str)->list:

    for i in range (len(lista)-1):

        for j in range (i+1, len(lista)):

            if lista [i][key] <  lista [j][key]:

                aux = lista [i]
                lista [i] = lista [j]
                lista [j] = aux                

    return lista

def ordenar_desc_lista_dic (lista:list,key:str)->list:

    for i in range (len(lista)-1):

        for j in range (i+1, len(lista)):

            if lista [i][key] >  lista [j][key]:

                aux = lista [i]
                lista [i] = lista [j]
                lista [j] = aux                

    return lista

