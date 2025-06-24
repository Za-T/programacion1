
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

    '''Verifica si el usuario quiere continuar el juego.

        Parametros
            pregunta =  texto de la pregunta a mostrar al usuario.

        Retorno: un booleano, 
            True si quiere continuar. 
            False si no quiere continuar.'''

    respuesta = validar_str (pregunta,"s","n")

    if respuesta == "s":
        respuesta = True
    else:
        respuesta = False

    return respuesta

def verificar_igualdad (valor1, valor2, verdad: str, falso: str) -> bool:

    '''Verifica si los parametros, valor1 y valor2, son iguales.

    Parametros:
        valor1: primer valor a comparar.
        valor2: seegundo valor a comparar.
        verdad: mensaje a mostrar si es verdadero.
        falso: mensaje a mostar si es falso.

    Retorno:
        True si es igual.
        False si no es igual.'''
    
    if valor1 == valor2:
        print (f"\n{verdad}")
        retornar = True
    else:
        print (f"\n{falso}")
        retornar = False
    
    return retornar

def verificar_existencia (lista: list) -> bool:

    '''La funcion verifica que la lista no este vacia.

    Parametro:
        lista: la lista que se busca comprobar.

    Retorno:
        True si existe
        False si no.'''

    try:
        lista [0]
        retornar = True
    except IndexError:
        retornar = False
    
    return retornar
