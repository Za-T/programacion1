from validaciones import *

def crear_menu (lista_opciones:list, lista_fun:list, datos: list):

    primero = 0
    ultimo = len(lista_opciones)
    
    repetir = "s"

    while repetir == "s":

        print ("\nMenu de opciones\n")
        
        for i in range(len(lista_opciones)):
            print (f"{i}. {lista_opciones[i]}")
        print ("\n")

        opcion = validar_int("opcion",primero,ultimo)

        lista_fun [opcion](datos)

        print ("\n")
        repetir = validar_str ("si quiere solicitar otra opcion", "s", "n")