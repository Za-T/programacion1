from csv import *

def escribir_score (ruta:str, nombre:str, puntos: int):

    anotar = [f"Nombre: {nombre}; ",
              f"Puntos: {puntos}; ",
              "\n"]

    with open(ruta, "a") as archivo:
        archivo.writelines(anotar)

def finalizar_juego (nombre:str, posicion:int,):

    print (f"\n{nombre} llego a la posicion {posicion}.")
    print (f"Fin del juego.")
    escribir_score("Score.csv", nombre, posicion)