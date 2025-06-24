
def solicitar_str (nombre_valor: str) -> str:

    '''Solicita al usuario el ingreso de una cadena y la retorna.
        Parametro:
            nombre_valor: el nombre del valor a ingresar'''
    
    cadena = str (input (f"Ingresar {nombre_valor}: "))
    return cadena

def validar_str (texto: str, op1: str, op2: str, op3: str = None) -> str:

    '''Validar que la cadena de caracteres ingresada este disponible entre 2 o 3 opciones.

    Parametros:
        texto: Texto que se muestra para indicarle al usuario que debe ingresar un valor. 
        op1: Opcion 1 a elegir
        op2: Opcion 2 a elegir,
        op3: Opcion 3 a elegir. Se asume que esta opcion esta vacia, 
        si en los parametros reales se ingresa un valor, entonces ahi se muestra esta opcion.

    Retorno:
        Retorna la respuesta elegida dentro de las opciones validas.'''

    if op3 != None:
        cadena = input (f"{texto} ({op1},{op2},{op3}): ")
        while cadena != op1 and cadena != op2 and cadena != op3:
            cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2},{op3}): "))

    else:
        cadena = input (f"{texto} ({op1},{op2}): ")
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
        valor2: segundo valor a comparar.
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
