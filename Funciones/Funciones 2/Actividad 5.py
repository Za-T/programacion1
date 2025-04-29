def encontrar_mas_grande (num1:int, num2:int, num3: int) -> int:

    '''Compara tres numeros, y retorna el mas grande'''
    
    if num1 > num2 and num1 > 3:
        return num1
    elif num2 > num3:
        return num2
    else:
        return num3
    
print (encontrar_mas_grande(50,200,-2))
