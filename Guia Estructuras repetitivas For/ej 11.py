limite = int (input("Ingrese numero: ")) 

contador_primos = 0
cont = 0

for i in range (1,limite):

    for j in range (1,limite):

            if i % j == 0:
                cont += 1
                
    if cont == 1:

        contador_primos += 1
        print (i)

        cont = 0

print ("Son en total {contador_primos}")
            



        
