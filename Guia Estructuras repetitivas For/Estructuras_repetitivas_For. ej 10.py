numero = int (input ("Ingrese numero: "))

numero_no_primo = False

if numero == 1:
    numero_no_primo == True
else:
    for i in range (2, numero):
        if i != numero and numero % i == 0:
            numero_no_primo = True


if numero_no_primo == True:
    print ("No es un numero primo.")
else:
    print ("Es un numero primo.")