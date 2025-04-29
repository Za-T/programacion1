#ej 13.

def validar_str (valor: str, op1: str, op2: str) -> str:

    '''Validar que la cadena de caracteres ingresada sea correcta'''

    cadena = str((input (f"Ingrese {valor} ({op1},{op2}): ")))

    while cadena != op1 and cadena != op2:
        cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2}): "))
    
    return cadena

respuesta = validar_str("respuesta", "s","n")
print (respuesta)

def validar_int (valor: str, desde: int, hasta: int) -> int:

    '''Validar que un numero, indicado por el usuario, 
    se encuentre en cierto rango'''

    entero = int (input (f"Ingrese {valor} en este rango ({desde} - {hasta}): "))

    while entero < desde or entero > hasta:
        entero = int (input (f"Error, valor invalido. Ingrese un nuevo valor en este rango ({desde} - {hasta}): "))

    return entero
    
numero = validar_int ("edad", 5, 10)

print (numero + 1)

def validar_float (valor: str, desde: float, hasta: float) -> float:

    '''Validar que un numero, indicado por el usuario, 
    se encuentre en cierto rango'''

    flotante = float (input (f"Ingrese {valor} en este rango ({desde} - {hasta}): "))

    while flotante < desde or flotante > hasta:
        flotante = float (input (f"Error, valor invalido. Ingrese un nuevo valor en este rango ({desde} - {hasta}): "))

    return flotante
    
numero = validar_float ("edad", 5.5, 10.5)

print (numero + 1)
