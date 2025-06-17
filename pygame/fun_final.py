from fun_score import *

def finalizar_juego (nombre:str, posicion:int,):

    print (f"\n{nombre} llego a la posicion {posicion}.")
    print (f"Fin del juego.")
    escribir_score("Score.csv", nombre, posicion)