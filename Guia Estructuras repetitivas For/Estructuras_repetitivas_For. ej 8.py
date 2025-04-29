numero = int (input ("Ingresar numero: "))

#i = 1 #pq no me deja definir 1? 

for lineas in range (numero + 1): #pq si no pogo + 1 no muestra el numero final? pq i epieza en 0 
    for num in range(1, lineas +1): 
        print(num, end="")
    print ("\n")

print ("Fin del programa.")

