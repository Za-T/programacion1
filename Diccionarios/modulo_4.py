from biblioteca_funciones import *

def promediar_edad (datos:list):

    key_list = ["legajo","nombre","apellido"]

    mostrar_keys (datos, key_list)
    
    suma_edad = 0
    #por cada elemento de la lista
    for e_dic in datos:
        suma_edad += e_dic["edad"]

    cant_edades = len(datos)
    promedio = suma_edad // cant_edades

    print (f"Contando a todos los estudiantes, la edad promedio es de {promedio}")
