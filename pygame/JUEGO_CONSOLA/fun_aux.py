
def solicitar_str (nombre_valor: str) -> str:
    '''Solicita al usuario el ingreso de una cadena y la retorna'''
    cadena = str (input (f"Ingresar {nombre_valor}: "))
    return cadena

def validar_str (valor: str, op1: str, op2: str, op3: str = None) -> str:

    '''Validar que la cadena de caracteres ingresada sea correcta'''

    if op3 != None:
        cadena = input (f"{valor} ({op1},{op2},{op3}): ")
        while cadena != op1 and cadena != op2 and cadena != op3:
            cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2},{op3}): "))

    else:
        cadena = input (f"{valor} ({op1},{op2}): ")
        while cadena != op1 and cadena != op2:
            cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2}): "))
    
    return cadena

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
