def sumar_digitos (numero:int,dividendo:int) -> int:

    '''Realizar una función recursiva que permita realizar la suma de los dígitos de un número: '''

    if numero == 0:
        return 0
    else:
        return numero % 10 + sumar_digitos (numero//10)
    
print (sumar_digitos(4569))