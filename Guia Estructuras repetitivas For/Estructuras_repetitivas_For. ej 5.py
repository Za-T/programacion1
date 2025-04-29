suma = 0
promedio = 0
iteraciones = 0



for i in range (10):
   
    numero = int (input ("Ingrese numero :"))
    
    if numero != 0:
        suma += numero
        iteraciones += 1
    else:
        break

if iteraciones != 0:
    promedio = suma / iteraciones

print (f"Fueron {iteraciones} iteraciones.")    
print (f"La suma total es: {suma}")
print (f"El promedio es:{promedio}")
print ("Fin del programa.")
