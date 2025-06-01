def calcular_promedio(lista:list, valor:int) -> bool: #parametros formales

    suma = 0

    for i in range (len(lista)):
        suma = suma + lista [i]
    
    promedio = suma / (len(lista)+1)

    if promedio > valor:
        retorno = True
    else:
        retorno = False
    
    return retorno

entrada = [10,20,30,40]
valor = 24

print (calcular_promedio(entrada , valor)) #invocacion #parametros actuales