def validar_int (valor: str, desde: int, hasta: int) -> int:

    '''Validar que un numero, indicado por el usuario, 
    se encuentre en cierto rango'''

    entero = int (input (f"Ingrese {valor} en este rango ({desde} - {hasta}): "))

    while entero < desde or entero > hasta:
        entero = int (input (f"Error, valor invalido. Ingrese un nuevo valor en este rango ({desde} - {hasta}): "))

    return entero

def solicitar_entero (nombre_valor: str) -> int:

    ''' Solicita al usuario el ingreso de un número entero y lo retorna'''
    entero = int(input (f"Ingresar {nombre_valor}: "))
    return entero

def validar_str (valor: str, op1: str, op2: str) -> str:

    '''Validar que la cadena de caracteres ingresada sea correcta'''

    cadena = str((input (f"Ingrese {valor} ({op1},{op2}): ")))

    while cadena != op1 and cadena != op2:
        cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2}): "))
    
    return cadena

#ej 1. DOCUMENTAR

'''def pedir_nombres ():

    nombres = [0] * 10

    for i in range (len(nombres)):
        nombres [i] = input ("Ingrese nombre: ")
        
    for i in range (len(nombres)):
        print (nombres [i])
    

print (pedir_nombres())'''

#ej 2. 

'''def armar_lista_numeros ()->list:

    lista_numeros = [0] * 10

    respuesta = "s"
     
    while respuesta == "s":

        posicion = validar_int ("posicion", 0, 9)

        numero = solicitar_entero ("numero")

        lista_numeros [posicion] = numero

        respuesta = validar_str ("si quiere insertar otro numero", "s", "n")

    return [lista_numeros]
        

print (armar_lista_numeros())
'''

#ej 3.

'''def armar_lista_rango () -> list:

    lista_rango = [0] * 10

    for i in range (len(lista_rango)):
        lista_rango [i] = validar_int("un numero",1,100)

    return lista_rango

print (armar_lista_rango())'''

#ej 4.

'''def buscar_dentro_lista (lista:list, numero_buscar: int) -> bool:

    for i in range (len(lista)):

        if numero_buscar == lista [i]:
            return True
        

lista_prueba = [21,31,45,68]

numero_buscar = int (input("Buscar numero: "))

print (buscar_dentro_lista(lista_prueba, numero_buscar))'''

#ej 5.

'''def buscar_menor_edad_nombres (edad_lista: list, nombre_lista:list):

    flag = True

    if flag == True:
        menor_edad = edad_lista [0]
        menor_nombre = nombre_lista [0]
        flag = False

    for i in range (len(edad_lista)):
        
        if edad_lista [i] <= menor_edad:
            menor_edad = edad_lista [i]
            menor_nombre = nombre_lista [i]

            print (menor_edad, menor_nombre)

nombres =["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria",
         "Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] 

edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43] 

print (buscar_menor_edad_nombres (edades, nombres))'''

#ej 6.

'''from listas_personas import *

lista_nombres = nombres

def mostrar_nombres (nombres:list):

    for i in range (len(nombres)):
        print (nombres [i])

print (mostrar_nombres(lista_nombres))
'''
#ej 7 - 8.

from listas_personas import *

'''nombres: list, telefonos:list, mail:list,adress:list,postalzip:list,region:list,country:list,edades:list
nombres[i] + telefonos [i] + mail [i] + adress [i] + postalZip [i] + region [i] + country [i] + edades [i]
(nombres,telefonos,mails,address,postalZip,region,country,edades)'''

def mostrar_datos_mexico (nombres: list, telefonos:list, mail:list,adress:list,postalzip:list,region:list,country:list,edades:list):

    for i in range (len(country)):

        if country [i] == "Mexico":

            print (nombres[i] + telefonos [i] + mail [i] + adress [i] + postalZip [i] + region [i] + country [i] + edades [i], sep = ", ")



def menu_estadisticas ()-> int:

    print ("Menu de Opciones: " \
    "\n1.Lista de los datos de los usuarios de México." \
    "\n2.Listar los nombre, mail y teléfono de los usuarios de Brasil." \
    "\n3.Listar los datos del/los usuario/s más joven/es." \
    "\n4.Obtener un promedio de edad de los usuarios." \
    "\n5.De los usuarios de Brasil, listar los datos del usuario de mayor edad." \
    "\n6.Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000." \
    "\n7.Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.")

    return validar_int("opcion",1,7)


print (menu_estadisticas())
print (mostrar_datos_mexico (nombres, telefonos, mails, address, postalZip, region, country, edades))

