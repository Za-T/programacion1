def escribir_csv (ruta:str, dato1:str, dato2: int):

    '''La funcion escribe los parametros, dato1 y dato2, dentro del archivo csv'''

    with open(ruta, "a") as archivo:
        archivo.write(f"{dato1},{dato2}\n")

def finalizar_juego (nombre:str, posicion:int,):

    '''La funcion se encarga de informar que el juego finalizo, a que posicion llego, 
    y ejecuta la funcion encargada de escribir los resultados en csv'''

    print (f"\n{nombre} llego a la posicion {posicion}.")
    print (f"Fin del juego.")
    escribir_csv("Score.csv", posicion, nombre)