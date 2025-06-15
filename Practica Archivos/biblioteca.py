def validar_str (valor: str, op1: str, op2: str) -> str:

    '''Validar que la cadena de caracteres ingresada sea correcta'''

    cadena = input (f"Ingrese {valor} ({op1},{op2}): ")

    while cadena != op1 and cadena != op2:
        cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2}): "))
    
    return cadena

def validar_int (valor: str, desde: int, hasta: int) -> int:

    '''Validar que un numero, indicado por el usuario, 
    se encuentre en cierto rango'''

    entero = int (input (f"Ingrese {valor} en este rango ({desde} - {hasta}): "))

    while entero < desde or entero > hasta:
        entero = int (input (f"Error, valor invalido. Ingrese un nuevo valor en este rango ({desde} - {hasta}): "))

    return entero

def crear_menu (lista_opciones:list, lista_fun:list, datos: list):

    primero = 0
    ultimo = len(lista_opciones)
    
    repetir = "s"

    while repetir == "s":

        print ("\nMenu de opciones\n")
        
        for i in range(len(lista_opciones)):
            print (f"{i}. {lista_opciones[i]}")
        print ("\n")

        opcion = validar_int("opcion",primero,ultimo)

        lista_fun [opcion](*datos[opcion])

        print ("\n")
        repetir = validar_str ("si quiere solicitar otra opcion", "s", "n")


