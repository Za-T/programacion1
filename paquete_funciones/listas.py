def mostrar_lista (lista:list):

    for i in range(len(lista)):
        print (f"\n{lista[i]}")

def buscar_mayor_lista (lista_num:list) -> int:

    '''Busca y retorna el mayor valor dentro de una lista'''

    flag = True

    for i in range (len(lista_num)):

        if flag == True:

                edad_mayor = lista_num [i]

                flag = False

        if lista_num [i] >= edad_mayor:
             
            edad_mayor = lista_num [i]

    return edad_mayor

def buscar_menor_lista (lista_num:list) -> int:

    '''Busca y retorna el menor valor dentro de una lista'''

    flag = True

    for i in range (len(lista_num)):

        if flag == True:

                edad_menor = lista_num [i]

                flag = False

        if lista_num [i] <= edad_menor:
             
            edad_menor = lista_num [i]

    return edad_menor

def ordenar_lista_ascendente (lista:list) -> list:
 
    for i in range(len(lista)-1):
        for j in range (i+1,len(lista)):
            if (lista [i] > lista[j]):
                aux = lista [i]
                lista [i] = lista [j]
                lista [j] = aux
    
    return lista 

def auxiliar_listas (lista:list,i,j):
    aux = lista [i]
    lista [i] = lista [j]
    lista [j] = aux

