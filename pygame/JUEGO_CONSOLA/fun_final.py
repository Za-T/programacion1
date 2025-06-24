def escribir_archivo (ruta:str, dato1:str, dato2: int):

    '''La funcion escribe los parametros, dato1 y dato2, dentro del archivo csv
        
        Parametros:
            ruta: ubicación del archivo.
            dato1: primer dato a guardar.
            dato2: segundo dato a guardar.
        '''

    with open(ruta, "a") as archivo:
        archivo.write(f"{dato1},{dato2}\n")

def finalizar_juego (nombre:str, posicion:int,):

    '''La funcion se encarga de informar que el juego finalizo, a que posicion llego, 
    y ejecuta la funcion encargada de escribir los resultados en csv
    
    Parametros:
        nombre: cadena con el nombre del jugador
        posicion: posición final en el tablero.'''

    print (f"\n{nombre} llego a la posicion {posicion}.")
    print (f"Fin del juego.")
    escribir_archivo("Score.csv", posicion, nombre)