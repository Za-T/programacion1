from listas_personas import *
from biblioteca_funciones import *

lista_nombres = nombres

def mostrar_nombres (nombres:list):

    for i in range (len(nombres)):
        print (nombres [i])

print (mostrar_nombres(lista_nombres))