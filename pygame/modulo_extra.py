from paquete_funciones.validaciones import *

def continuar_juego (pregunta:str) -> bool:

    respuesta = validar_str (pregunta,"s","n")

    if respuesta == "s":
        respuesta = True
    else:
        respuesta = False

    return respuesta