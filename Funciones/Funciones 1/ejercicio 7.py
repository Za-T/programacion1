from Biblioteca_de_Funciones import * 

numero1 = validar_num (10,100)
numero2 = validar_num (10,100)

operacion = validar_str ("s","r")

if operacion == "s":
    print (sumar (numero1,numero2))
else:
    print (restar (numero1,numero2))

print ("Fin del programa")
