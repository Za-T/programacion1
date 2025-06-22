from csv import *

def leer_csv (nombre:str)-> list:
    
    try:
        with open(nombre, 'r') as archivo:
            
            lista_lineas = archivo.readlines()

            for linea in lista_lineas:
                print(linea, end="")

        return lista_lineas
    
    except FileNotFoundError:
        print ("Ese archivo no existe.")


print (leer_csv("score.csv"))