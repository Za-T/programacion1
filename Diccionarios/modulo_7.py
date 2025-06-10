from biblioteca_funciones import *

'''\n7.Listar legajo, nombre, apellido y programas que cursan los alumnos más jóvenes. \n'''

key_list = ["legajo", "nombre", "apellido", "programas"]


def listar_jovenes (datos:list):

    primer = True
    
    list_menor = []

    for estudiantes in datos:

        if primer == True:
            edad_menor = estudiantes ["edad"]
            primer = False

        elif estudiantes ["edad"] < edad_menor:
            edad_menor = estudiantes ["edad"]
            
    for estudiantes in datos:

        if estudiantes ["edad"] == edad_menor:
            list_menor.append (asignar_valores (estudiantes))
    
            
    for estudiante in list_menor:

        print (f"El estudiante se llama {estudiante ["nombre"]} {estudiante ["apellido"]}, su legajo es {estudiante ["legajo"]}, y esta en el programa {estudiante ["programa"]}.")