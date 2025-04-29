def muestrar_validar_num (desde,hasta):
    '''Validar que un numero se encuentre en cierto rango'''
    num = int (input ("Ingrese numero: "))

    if num < desde or num > hasta:
        print ("Numero no valido.")
    else:
        print (f"El numero {num} esta dentro del rango")


minimo = int (input ("Ingrese minimo del rango: "))
maximo = int (input ("Ingrese maximo del rango: "))

muestrar_validar_num (minimo,maximo)