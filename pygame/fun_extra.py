from paquete_funciones.validaciones import *

def continuar_juego (pregunta:str) -> bool:

    respuesta = validar_str (pregunta,"s","n")

    if respuesta == "s":
        respuesta = True
    else:
        respuesta = False

    return respuesta

def verificar_igualdad (valor1, valor2, verdad: str, falso: str) -> bool:
    
    if valor1 == valor2:
        print (f"\n{verdad}")
        retornar = True
    else:
        print (f"\n{falso}")
        retornar = False
    
    return retornar
