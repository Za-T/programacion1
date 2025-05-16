def validar_int (minimo:int,maximo:int) -> int:
    
    numero = int(input ("Elija numero "))

    if numero < minimo or numero > maximo:

        numero = int(input ("Error. Elija numero "))

    return numero

def verificar_coordenadas(tablero:list, x:int,  y:int) -> bool:
            
            if tablero [x][y] == 1:
                hundido = True
            else:
                hundido = False
            return hundido

tablero = [[0,0,1,0,0],
           [0,1,0,1,0],
           [1,0,0,1,0],
           [0,0,1,0,1],
           [0,0,0,0,1]]

barcos_hundidos = 0               
seguir = "s"
        
while seguir == "s":
     
    corrdenada_x = validar_int(0,4)
    coordenada_y =  validar_int (0,4)

    acierto = verificar_coordenadas (tablero,corrdenada_x,coordenada_y)
            
    if acierto == True:
         print ("Hundido")
         barcos_hundidos += 1
    else:
         print ("Agua")

    seguir = input ("Seguir (s/n):")

print (f"Barcos hundidos:{barcos_hundidos}")
