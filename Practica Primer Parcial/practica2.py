numeros = [10,20,30,40,50]
numero_comp = 24

def comparar_promedio (lista_num:list,comparador:int) -> bool: #parametros formales

    '''La funcion comparar_promedio, suma una lista de numeros, lo divide por la cantidad de elementos en la lista 
        Una vez obtiene el promedio lo compara con el parametro de comparador y verifica cual es mas grande.
        Si el promedio de la lista es mas grande, retorna True.
        Si eel numero en parametro es mas grande, retorna False. 
    '''

    suma = 0
    cant_num = (len(lista_num))
    

    for i in range (len(lista_num)):
        suma += lista_num [i]
    print (suma)

    if cant_num != 0:
        promedio = suma / cant_num
    else:
        promedio = 0
    
    print (promedio)


    if promedio > comparador:
        resultado = True 
    else:
        resultado = False

    return resultado

print (comparar_promedio(numeros, numero_comp)) #parametros reales


