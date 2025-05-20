def verificar_tesoro (mapa:list, x:int, y:int) ->int:

    if mapa [x][y] == 1:
        distancia = 0

    else:
        distancia = (x - 1) + (y - 3)
        distancia = distancia * (-1)

    return distancia


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
            x = int(input("Error. Ingrese coordenada de fila (0-4): "))

        y = int (input ("Ingrese coordenada de columna (0-4): "))
        if y < 0 or y > 4:
            y = int(input("Error. Ingrese coordenada de columna (0-4): "))


        resultado = verificar_tesoro(mapa, x, y)

        if resultado == 0:

            print ("Encontraste el tesoro!")

            repetir = "n"

        else:

            print (f"Fallaste. El tesoro está a {resultado} casilleros de distancia.")

            repetir = input("Quiere repetir (s/n)? ")

            if repetir != "s" and repetir != "n":
                repetir = input("Error. Quiere repetir (s/n)? ")

radar_del_tesoro ()