from estudiantes import *
from biblioteca_funciones import *


def mostrar_keys (datos:list, key_list: list):

    for i in range(len(datos)):
        for j in range (len(key_list)):
            print (f"{key_list[j]}: {datos[i][key_list[j]]}")
        print ("\n")

def listar_apellido_asc (datos:list):

    key_list = ["legajo","nombre", "apellido"]

    for i in range (len(datos)-1):
        for j in range (i+1,len(datos)):

            if (datos[i]["apellido"]) > (datos[j]["apellido"]):
                auxiliar_listas (datos,i,j)

            elif (datos[i]["apellido"]) == (datos[j]["apellido"]):
                if (datos[i]["nombre"]) > (datos[j]["nombre"]):
                    auxiliar_listas (datos,i,j)
    
    mostrar_keys (datos, key_list)
            



        

listar_apellido_asc (estudiantes)