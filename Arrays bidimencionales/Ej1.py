productos = [[[None], ["botellas", 3], [None], ["frasco", 8], [None]],
             [[None],[None],["fideos",4],[None],[None]],
             [[None],[None],[None],["leche",6],[None],]]

def dar_alta (producto:list = productos):

    nombre = input("\nIngrese nombre del nuevos producto: ")

    cantidad = int (input ("\nIngrese cantidad:"))

    fila = int (input ("\nIngrese en que fila se coloca (0-2):"))
    
    columna = int (input ("\nIngrese en que columna se coloca (0-4):"))

    if productos [fila] [columna] != :
        print ("k")

def elegir_menu ():

    repetir = "s"

    while repetir == "s":

        seleccionar = int (input("Elegir opcion del menu (1-6): "))

        match seleccionar:

            case 1:
                dar_alta ()
        
        repetir = input ("Quiere seleccionar otra opcion (s/n): ")

        while repetir != "s" and repetir != "n":
            repetir = input ("Quiere seleccionar otra opcion (s/n): ")
        

elegir_menu () 