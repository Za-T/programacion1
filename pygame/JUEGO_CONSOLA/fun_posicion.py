def actualizar_posicion_mov (tablero:list, posicion: int, resultado_res:bool) -> int:
    
    '''La funcion se encargar de verificar cual es la nueva posicion a la que se tiene que mover el jugador.
        Ademas le informa si cayo en escalera o serpiente, y cuantos casilleros debe saltearse.
        
        Parametros:
            tablero: lista que representa el orden del tablero.
            posicion: posición actual del jugador.
            resultado_res: valor booleano que indica si fue correcta la respuesta del jugador.
        
        Retorno:
          Un entero con la nueva posicion.'''

    if posicion != 0 and posicion != 30:
       
        if resultado_res == True:

            posicion += 1

            if tablero [posicion] != 0:
                print (f"Caiste en escalera, adelantas {tablero [posicion]} casilleros.\n")
                posicion += tablero [posicion]

        else:

            posicion -= 1

            if tablero [posicion] != 0:            
                print (f"Caiste en serpiente, regresas {tablero [posicion]} casilleros.\n")
                posicion -= tablero [posicion]

    return posicion
