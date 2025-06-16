def calcular_posicion (tablero:list, posicion: int, resultado_res:bool) -> int:
    
    if posicion != 0 and posicion != 30:
       
        if resultado_res == True:
            estado = posicion + 1
        else:
            estado = posicion - 1
    else:
        estado = posicion 

    return estado
