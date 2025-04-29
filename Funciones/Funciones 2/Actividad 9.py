'''def creador_tabla_multiplicar (factor: int, inicio: 1,  fin = 10):

    for i in range (inicio, fin+1):
    
        resultado = factor * i
        print (f"{factor} * {i} = {resultado}")

        #return f"{factor} * {i} = {resultado}" #pq cuando escribo asi solo retorna una vez?
                  
    
print (creador_tabla_multiplicar (1))'''


def creador_tabla_multiplicar (factor: int, inicio: 1, fin = 10, multiplicador = int): 
    #el fin no funciona correctamente, una vez llegado al numero ingresado se reescribe con 10
    
    '''La funcion imprime la tabla de multiplicar de un número recibido como 
        parámetro. La función acepta parámetros opcionales (inicio y fin) para definir 
        el rango de multiplicación. Por defecto es del 1 al 10.'''

    multiplicador = inicio

    if multiplicador != fin:
        resultado = factor * multiplicador
        print (f"{factor} * {multiplicador} = {resultado}")
        return creador_tabla_multiplicar (factor, multiplicador +1)
    else:
        resultado = factor * multiplicador
        return (f"{factor} * {multiplicador} = {resultado}")

print (creador_tabla_multiplicar (1))