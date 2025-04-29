def verificador_par (num:int) -> str:

    '''Verifica si un numero es par o impar'''

    if num % 2 == 0:
        return "Es par."
    else:
        return "Es impar."

x = int (input ("Imgrese un numero:"))

print (verificador_par(x))