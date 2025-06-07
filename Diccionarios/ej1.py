from estudiantes import *
from biblioteca_funciones import *

def seleccionar_menu_estadisticas ():

    '''Permite seleccionar que estadistica se quiere ver, y da la opcion de seleccionar otra al final'''

    repetir = "s"

    while repetir == "s":

        print ("Menu de Opciones:" \
        "\n1.Listar los alumnos por orden ascendente de apellido, si se repite, ordenar por nombre. Mostrar legajo, nombre, apellido y edad ." 
        "\n2.Obtener el promedio de notas para cada estudiante ." \
        "\n3.Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa de “Ingenieria en Informatica." \
        "\n4.Obtener un promedio de edad de los estudiantes. Mostrar nombre y apellido. " \
        "\n5.Informar el alumno con mayor pomedio de notas. Mostrar nombre y apellido ." \
        "\n6.Listar nombre y apellido de los alumnos que forman el grupo “Club de Informática” con sus respectivos promedios." \
        "\n7.Listar legajo, nombre, apellido y programas que cursan los alumnos más jóvenes. \n")

        opcion = validar_int("opcion",1,7)

        match opcion:
            case 1:
                print()
            case 2:
                print()
            case 4:
                print ()
            case 5:
                print ()
            case 6:
                print ()
            case 7:
                print ()

        repetir = validar_str ("si quiere solicitar otra opcion", "s", "n")

seleccionar_menu_estadisticas()