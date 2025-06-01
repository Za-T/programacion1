tablero = [["O",None,"X"],
           ["X","O","X"],
           ["O",None,"O"],]

def validar_pieza ()-> str:

    pieza = input("Ingrese que pieza va acolocar (X-O): ")

    while pieza != "X" and pieza != "O":
        pieza = input("Error, pieza no valida. Ingrese que pieza va acolocar (X-O): ")

    return pieza

def validar_int (minimo:int, maximo:int, valor:str)-> int:

    numero = int (input(f"Ingrese en que {valor} va acolocar ({minimo}-{maximo}): "))

    while numero < minimo or numero > maximo:
        numero = int (input(f"Error, {valor} no valido. Ingrese en que {valor} va acolocar ({minimo}-{maximo}): "))
    return numero

def mostrar_tablero (lista_brut:list):

    for i in range (len(lista_brut)):

        for j in range (len(lista_brut)):
            print (f"|{tablero[i][j]}|", end = "")
    
        print ("\n")
        
def colocar_pieza (tablero:list, tipo_pieza:str):

    fila = validar_int(0, 2, "fila")
    columna = validar_int(0, 2, "columna")

    while tablero [fila][columna] != None:
        
        print ("\nError. Lugar de pieza ocupado, elija otro")

        fila = int (input(f"\nElija en que fila colocar {tipo_pieza} (0-2): "))
        columna = int (input(f"Elija en que columna colocar {tipo_pieza} (0-2): "))

    tablero [fila][columna] = tipo_pieza
        
def comprobar_estado (tablero:list):

    estado = True

    while estado == True:

        for i in range (len (tablero)):

            if (tablero [i] [0] == tablero [i] [1]) and (tablero [i][1] == tablero [i][2]):
                print (f"Gano {tablero[i][0]}")
                estado = False
                
            elif (tablero [0] [i] == tablero [1] [i]) and (tablero [1][i] == tablero [2][i]):
                print (f"Gano {tablero[0] [i]}")
                estado = False

            elif (tablero [0] [0] == tablero [1] [1]) and (tablero [1][1] == tablero [2][2]):
                print (f"Gano {tablero[0] [0]}")
                estado = False
            
            
    
            

def jugar_tateti (tablero:list):

    repetir = "s"

    while repetir == "s":

        mostrar_tablero (tablero)

        '''pieza = validar_pieza ()

        colocar_pieza (tablero, pieza)
    
        mostrar_tablero (tablero)'''

        comprobar_estado (tablero)

        repetir = input ("quiere agregar otra pieza? (s-n)")

jugar_tateti(tablero)