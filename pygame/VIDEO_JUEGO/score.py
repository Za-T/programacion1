from csv import *

def leer_csv (nombre:str)-> list:
    
    try:
        with open(nombre, 'r') as archivo:
            lista_lineas = archivo.readlines()

        return lista_lineas
    
    except FileNotFoundError:
        print ("Ese archivo no existe.")
