def verificador_par (num:int) -> bool:

    '''Verifica si es par o impar, y retorna un valor booleano,True si es par, False si es impar.'''

    return  num % 2 == 0

x = int (input ("Imgrese un numero:"))

print (verificador_par(x))