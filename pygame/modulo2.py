def calcular_posicion (tablero:list, posicion: int, resultado_res:bool) -> int:
    
    if posicion != 0 and posicion != 30:
       
        if resultado_res == True:

            posicion += 1

            if tablero [posicion] != 0:
                print (f"Caiste en escalera, adelantas {tablero [posicion]} casilleros.")
                posicion += tablero [posicion]

        else:

            posicion -= 1

            if tablero [posicion] != 0:            
                print (f"Caiste en serpiente, atrasas {tablero [posicion]} casilleros.")
                posicion -= tablero [posicion]
                

    else:
        posicion = posicion 

    return posicion
