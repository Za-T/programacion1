def sumar_digitos (numero:int,dividendo:int) -> int:

    if numero == 0:
        return 0
    else:
        print (numero, dividendo)
        numero = numero // dividendo 
        return (sumar_digitos (numero, dividendo * 10))

numero = int (input ("Ingrese numero: "))

print (sumar_digitos(numero, 1))

'''print (numero // 1000)

if numero == 0:
valor1= numero // 100 
print (valor1)
valor2 = (numero - (valor1 * 100)) // 10
print (valor2)
valor3 = numero - ((valor2 * 10 ) + (valor1 * 100))
print (valor3)

repeticiones = 1 * 10
'''
