Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"] 
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98] 

def ordenar_n_asc_p_des (list1: list, list2: list):

    for i in range(len(list1)-1):

        for j in range (i+1,len(list1)):

            if (list1 [i] > list1[j]):

                aux = list1 [i]
                aux2 = list2[i]
                list1 [i] = list1 [j]
                list2 [i] = list2 [j]
                list1 [j] = aux
                list2 [j] = aux2

            elif (list1 [i] == list1 [j]):

                if (list2 [i] < list2[j]):

                    aux2 = list2 [i]
                    aux = list1 [i]
                    list2 [i] = list2 [j]
                    list1 [i] = list1 [j]
                    list2 [j] = aux2
                    list1 [j] = aux

ordenar_n_asc_p_des (Nombres, Puntos)

print (Nombres)
print (Puntos) 