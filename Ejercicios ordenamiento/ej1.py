def mostrar_lista (lista:list):

    for i in range(len(lista)):
        print (lista[i])

Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] 
Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]    

def ordenar_dos_listas_ascendente (list1: list, list2: list):

    for i in range(len(list1)-1):

        for j in range (i+1,len(list1)):

            if (list1 [i] > list1[j]):

                aux = list1 [i]
                aux2 = list2[i]
                list1 [i] = list1 [j]
                list2 [i] = list2 [j]
                list1 [j] = aux
                list2 [j] = aux2

mostrar_lista (Nombres)
mostrar_lista (Edades)
