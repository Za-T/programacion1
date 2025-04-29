numero = int (input ("Ingrese numero: "))

x = 1
contador_primos = 0
numero_primo = 0

if numero ==  1:
    print ("No es numero primo.")

for i in range (numero):
        
        '''numero_primo += 1
        x += 1

        if x != 2 and x % 2 == 0:
            print (" ")
        
        else:
        if x != numero_primo and numero_primo % x == 0:
            print ("")
        else:
            print (f"{numero_primo}")
            contador_primos += 0

if numero != 2 and x % 2 == 0 :
    print ("")
else:
    for i in range (numero):
        numero_primo += 1
        x += 1
        if x != numero_primo and numero_primo % x == 0:
            print ("")
        else:
            print (f"{numero_primo}")
            contador_primos += 0 '''

print (f"Se encontraron {contador_primos} numeros primos.")
print ("Fin del programa.")