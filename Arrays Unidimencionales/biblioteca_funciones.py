def validar_int (valor: str, desde: int, hasta: int) -> int:

    '''Validar que un numero, indicado por el usuario, 
    se encuentre en cierto rango'''

    entero = int (input (f"Ingrese {valor} en este rango ({desde} - {hasta}): "))

    while entero < desde or entero > hasta:
        entero = int (input (f"Error, valor invalido. Ingrese un nuevo valor en este rango ({desde} - {hasta}): "))

    return entero

def solicitar_entero (nombre_valor: str) -> int:

    ''' Solicita al usuario el ingreso de un número entero y lo retorna'''
    entero = int(input (f"Ingresar {nombre_valor}: "))
    return entero

def validar_str (valor: str, op1: str, op2: str) -> str:

    '''Validar que la cadena de caracteres ingresada sea correcta'''

    cadena = str((input (f"Ingrese {valor} ({op1},{op2}): ")))

    while cadena != op1 and cadena != op2:
        cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2}): "))
    
    return cadena