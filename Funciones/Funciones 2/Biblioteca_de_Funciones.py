def calcular_descuento (valor:int, descuento:int) -> int:

    '''Calcular el valor total del descuento'''
    descuento_total = (valor * descuento) / 100
    return valor - descuento_total

def validar_int (valor: str, desde: int, hasta: int) -> int:

    '''Validar que un numero, indicado por el usuario, 
    se encuentre en cierto rango'''

    entero = int (input (f"Ingrese {valor} en este rango ({desde} - {hasta}): "))

    while entero < desde or entero > hasta:
        entero = int (input (f"Error, valor invalido. Ingrese un nuevo valor en este rango ({desde} - {hasta}): "))

    return entero

def validar_float (valor: str, desde: float, hasta: float) -> float:

    '''Validar que un numero, indicado por el usuario, 
    se encuentre en cierto rango'''

    flotante = float (input (f"Ingrese {valor} en este rango ({desde} - {hasta}): "))

    while flotante < desde or flotante > hasta:
        flotante = float (input (f"Error, valor invalido. Ingrese un nuevo valor en este rango ({desde} - {hasta}): "))

    return flotante

def sumar (num1: float, num2: float) -> float:
    '''Realiza la suma de dos numeros'''
    return num1 + num2

def restar (num1: float, num2: float) -> float:
    '''Realiza la resta de dos numeros'''
    return num1 - num2

def validar_str (valor: str, op1: str, op2: str) -> str:

    '''Validar que la cadena de caracteres ingresada sea correcta'''

    cadena = str((input (f"Ingrese {valor} ({op1},{op2}): ")))

    while cadena != op1 and cadena != op2:
        cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2}): "))
    
    return cadena

def solicitar_entero (nombre_valor: str) -> int:
    ''' Solicita al usuario el ingreso de un número entero y lo retorna'''
    entero = int(input (f"Ingresar {nombre_valor}: "))
    return entero

def solicitar_float (nombre_valor: str) -> float:
    '''Solicita al usuario el ingreso de un número flotante y lo retorna'''
    flotante = float (input (f"Ingresar {nombre_valor}: "))
    return flotante
    
def solicitar_str (nombre_valor: str) -> str:
    '''Solicita al usuario el ingreso de una cadena y la retorna'''
    cadena = str (input (f"Ingresar {nombre_valor}: "))
    return cadena

#sdsdsd