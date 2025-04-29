from biblioteca_funciones import *

def buscar_dentro_lista (lista:list, numero_buscar: int) -> bool:

    for i in range (len(lista)):

        if numero_buscar == lista [i]:
            return True
        

lista_prueba = [21,31,45,68]

numero_buscar = int (input("Buscar numero: "))

print (buscar_dentro_lista(lista_prueba, numero_buscar))