def verificar_tesoro (mapa:list, x:int, y:int) ->int:

    if mapa [x][y] == 1:
        devolver = 0
    else:
        devolver = (x - 1) + (y - 3)
    
    return devolver


def radar_del_tesoro ():

    repetir = "s"

    mapa = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0] ]

    while repetir == "s":

        
        x = int (input ("Ingrese coordenada de fila (0-4): "))

        if x < 0 or x > 4:

            repetir = input("Error. Ingrese coordenada de fila (0-4): ")

        y = int (input ("Ingrese coordenada de columna (0-4): "))

        if y < 0 or y > 4:
            repetir = input("Error. Ingrese coordenada de columna (0-4): ")


        resultado = verificar_tesoro(mapa, x, y)

        if resultado == 0:

            print ("Encontraste el tesoro!")

            repetir = "n"

        else:

            print (f"Fallaste. El tesoro está a {resultado} casilleros de distancia.")

            repetir = input("Quiere repetir (s/n)? ")

            '''while repetir != "s" or repetir != "n":
                repetir = input("Error. Quiere repetir (s/n)? ")'''

radar_del_tesoro ()