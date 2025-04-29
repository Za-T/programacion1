numero = int(input("Ingresar numero: "))

divisor = 0
cant_div = 0

while numero == 0:
     numero = int (input("Numero invalido. Ingresar otro numero: "))

while numero != divisor :
    
    divisor += 1
    
    if numero % divisor == 0:
       print (f"{divisor}")
       cant_div += 1

print (f"La cantidad de divisores encontrados es de: {cant_div}.")
print ("Fin del programa.")