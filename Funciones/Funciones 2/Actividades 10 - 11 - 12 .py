#ej 10.

def solicitar_entero (nombre_valor: str) -> int:
    ''' Solicita al usuario el ingreso de un número entero y lo retorna'''
    entero = int(input (f"Ingresar {nombre_valor}: "))
    return entero

#ej 11.

def solicitar_float (nombre_valor: str) -> float:
    '''Solicita al usuario el ingreso de un número flotante y lo retorna'''
    flotante = float (input (f"Ingresar {nombre_valor}: "))
    return flotante

#ej 12.

def solicitar_str (nombre_valor: str) -> str:
    '''Solicita al usuario el ingreso de una cadena y la retorna'''
    cadena = str (input (f"Ingresar {nombre_valor}: "))
    return cadena
