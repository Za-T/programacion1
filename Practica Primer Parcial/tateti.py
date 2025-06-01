tablero = [[None,None,None],
           [None,None,None],
           [None,None,None],]

def mostrar_tablero (lista_brut:list):

    for i in range (len(lista_brut)):

        for j in range (len(lista_brut)):
            print (f"|{tablero[i][j]}|", end = "")
    
        print ("\n")
        
def colocar_pieza (tablero:list, tipo_pieza:str):

    fila = int (input(f"\nElija en que fila colocar {tipo_pieza} (0-2): "))
    columna = int (input(f"Elija en que columna colocar {tipo_pieza} (0-2): "))

    while tablero [fila][columna] != None:
        
        print ("\nError. Lugar de pieza ocupado, elija otro")

        fila = int (input(f"\nElija en que fila colocar {tipo_pieza} (0-2): "))
        columna = int (input(f"Elija en que columna colocar {tipo_pieza} (0-2): "))

    tablero [fila][columna] = tipo_pieza
        

def jugar_tateti (tablero:list):

    repetir = True

    while repetir == True:

        mostrar_tablero (tablero)

        pieza = input("Ingrese que pieza va acolocar (X-O): ")

        colocar_pieza (tablero, pieza)
    
        mostrar_tablero (tablero)

        repetir = False

jugar_tateti (tablero)