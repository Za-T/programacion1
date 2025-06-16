from paquete_funciones.validaciones import *

def continuar_juego (pregunta:str) -> bool:

    respuesta = validar_str (pregunta,"s","n").lower()

    if respuesta == "s":
        respuesta = True
    else:
        respuesta = False

    return respuesta

def verificar_existencia (lista: list) -> bool:

    try:
        lista [0]
        retornar = True
    except IndexError:
        retornar = False
    
    return retornar