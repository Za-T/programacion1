from biblioteca_funciones import *

def buscar_menor_edad_nombres (edad_lista: list, nombre_lista:list):

    '''La funcion recibe por parámetro la lista de edades, busca a las 
        personas de menor edad (puede ser más de una) y las retorna.'''

    flag = True

    if flag == True:
        menor_edad = edad_lista [0]
        menor_nombre = nombre_lista [0]
        flag = False

    for i in range (len(edad_lista)):
        
        if edad_lista [i] <= menor_edad:
            
            menor_edad = edad_lista [i]
            menor_nombre = nombre_lista [i]

            print (menor_edad, menor_nombre)

nombres =["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria",
         "Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] 

edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43] 

buscar_menor_edad_nombres (edades, nombres)