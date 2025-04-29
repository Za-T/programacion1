#ej 1.
def mostrar_numero (numero):
    return numero

print (mostrar_numero (50))

#ej 2.

def ingreso_num (num):
    num = input ("Entre un numero:")
    return num

print (ingreso_num (0))

#ej 3.

def determinar_par (num):
    return bool (num % 2 == 0)

x = int (input ("Ingrese un numero:"))
print (determinar_par(x))

# ej 4.

def muestrar_validar_num (desde:int,hasta:int)->int:

    num = int (input ("Ingrese numero: "))

    if num < desde or num > hasta:
        print ("Numero no valido.")
    else:
        print (f"El numero {num} esta dentro del rango")


minimo = int (input ("Ingrese minimo del rango: "))
maximo = int (input ("Ingrese maximo del rango: "))

muestrar_validar_num (minimo,maximo)

#ej 5.

def restar1 (valor_a: int, valor_b: int) -> int:
    return valor_a - valor_b

print (restar1(5,1))

def restar2 (valor_a,valor_b) -> int:
    diferencia = valor_a - valor_b
    return diferencia

print (restar2(5,1))

def restar3 (valor_a: int, valor_b: int):
    return valor_a - valor_b

print (restar3(5,1))

def restar4 (valor_a, valor_b):
    diferencia = valor_a - valor_b
    return diferencia

print (restar4 (5,1))

#ej 6.

def realizar_descuento (valor:int, descuento = 5) -> int:
    descuento_total = (valor * descuento) / 100
    return valor - descuento_total

def validar (num: int) -> int:
    
    while num < 10 or num > 100:
        num = int (input ("Error, valor invalido. Ingrese un nuevo valor: ")) 
    
    return num
       
numero1 = int (input ("Ingrese un valor: "))

numero1 = validar (numero1)

print ("El valor una vez aplicado el descuento es", realizar_descuento (numero1))

#ej 7.

from Biblioteca_de_Funciones import * 

numero1 = validar_num (10,100)
numero2 = validar_num (10,100)

operacion = validar_str ("s","r")

if operacion == "s":
    print (sumar (numero1,numero2))
else:
    print (restar (numero1,numero2))

print ("Fin del programa")

