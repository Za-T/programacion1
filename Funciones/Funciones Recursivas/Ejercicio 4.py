def calcular_fibonacci (numero:int) -> int:

    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return calcular_fibonacci (numero - 1) + calcular_fibonacci (numero - 2)
    
print (calcular_fibonacci (9))