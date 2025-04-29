import random

def verificar_ganador_ronda (jugador:int, maquina:int) -> str:

    if jugador == maquina:
        ganador = "Empate"
    
    else: 
        match jugador:

            case 1:
                    if maquina == 2:
                        ganador = "Maquina"
                    else:
                        ganador = "Jugador"
            case 2:
                    if maquina == 3:
                        ganador = "Maquina"
                    else:
                        ganador = "Jugador"
            case 3:
                    if maquina == 1:
                        ganador = "Maquina"
                    else:
                        ganador = "Jugador"

    return f"El ganador de esta ronda fue: {ganador}"      

def verificar_estado_partida (aciertos_jugador:int, aciertos_maquina:int, ronda_actual:int = 0) -> bool:

    if ronda_actual <= 3 and (aciertos_jugador or aciertos_maquina) == 2:
        return False
    else:
        return True

def verificar_ganador_partida (aciertos_jugador, aciertos_maquina) -> str :

    if aciertos_jugador > aciertos_maquina:
        return "Jugador"
    else:
        return "Maquina"

def mostrar_elemento(eleccion:int) -> str:
    
    match eleccion:
        case 1:
            return "Piedra"
        case 2:
            return "Papel"
        case 3:
            return "Tijera"

def jugar_piedra_papel_tijera () -> str:

    eleccion_jugador = int(input ("Elija (1-2-3): "))

    print ("Usted eligio:", mostrar_elemento (eleccion_jugador))

    eleccion_maquina = random.randint(1,3)
    
    print ("La maquina eligio:", mostrar_elemento (eleccion_maquina))

    ganador_ronda = verificar_ganador_ronda (eleccion_jugador, eleccion_maquina)

    if ganador_ronda == "Jugador":
        aciertos_jugador += 1 
    elif ganador_ronda == "Maquina":
        aciertos_maquina += 1

    verificar_estado_partida (aciertos_jugador, aciertos_maquina)

    print ("El ganador es: ", verificar_ganador_partida (aciertos_jugador, aciertos_maquina))

    
print (jugar_piedra_papel_tijera())
