'''Ejercicio 3: 
Ingresar 5 números enteros, distintos de cero.  
Informar: 
a. Cantidad de pares e impares. 
b. El menor número ingresado. 
c. De los pares el mayor número ingresado. 
d. Suma de los positivos. 
e. Producto de los negativos. '''

pares= 0
impares = 0 
total = 0
numero= 0
suma_pos = 0
producto_neg = 1
numero_menor = 0
flag = True
flag_neg = True

for i in range (5):

    numero = int (input("Ingrese numero: "))

    if numero == 0: 
        print ("Datos invalidos.")

    else: 

        if (numero % 2) == 0:
            pares += 1
            if flag == True:
                par_mayor = numero
                flag = False
            elif numero > par_mayor:
                par_mayor = numero

        else:
            impares += 1

    #el menor numero ingresado

    if i == 0:
        numero_menor = numero 
    elif numero < numero_menor:
         numero_menor = numero 

    
    if numero > 0:
        suma_pos += numero
    else:
        flag_neg = False
        producto_neg *= numero 


    total += numero


print ("La cantidad de numeros pares es de:", pares)
print ("La cantidad de numeros impares es de:", impares)
print ("El numero menor ingresado es:", numero_menor)
print ("La suma de los numeros positivos ingresados es de:", suma_pos)

if flag_neg == False :
    print ("El producto de los numeros negativos ingresados es de:", producto_neg)
else:
    print ("No hay numeros negativos.")

print ("La suma de los numero ingresados es de:", total)