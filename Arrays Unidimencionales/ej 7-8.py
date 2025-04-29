from listas_personas import *
from biblioteca_funciones import *


def mostrar_datos_mexico (nombres: list, telefonos:list, mail:list,adress:list,postalzip:list,region:list,country:list,edades:list):

    for i in range (len(country)):

        if country [i] == "Mexico":

            print (nombres[i], telefonos [i], mail [i], adress [i], postalZip [i], region [i], country [i], edades [i], sep = ", ")

def mostrar_datos_brazil  (nombres: list, telefonos:list, mail:list):
    
    for i in range (len(country)):
        if country [i] == "Brazil":
            print (nombres[i], telefonos [i], mail [i], sep = ", ")

def mostrar_datos_jovenes (nombres: list, telefonos:list, mail:list,adress:list,postalzip:list,region:list,country:list,edades:list):

    edad_menor = edades [0]

    for i in range (len(edades)):

        if edades [i] <= edad_menor:
            print (nombres[i], telefonos [i], mail [i], adress [i], postalZip [i], region [i], country [i], edades [i], sep = ", ")

def promediar_edad (edades:list) ->int:

    suma_edades = 0
    total_edades = 0

    for i in range (len(edades)) :

        suma_edades += edades [i]
        total_edades += 1

    promedio_edades = suma_edades // total_edades

    return promedio_edades



def menu_estadisticas ():

    print ("Menu de Opciones: \n" \
    "\n1.Lista de los datos de los usuarios de México." \
    "\n2.Listar los nombre, mail y teléfono de los usuarios de Brasil." \
    "\n3.Listar los datos del/los usuario/s más joven/es." \
    "\n4.Obtener un promedio de edad de los usuarios." \
    "\n5.De los usuarios de Brasil, listar los datos del usuario de mayor edad." \
    "\n6.Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000." \
    "\n7.Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.")

    opcion = validar_int("opcion",1,7)

    match opcion:
        case 1:
            mostrar_datos_mexico(nombres, telefonos, mails, address, postalZip, region, country, edades)
        case 2:
            mostrar_datos_brazil (nombres, telefonos, mails)
        case 3:
            mostrar_datos_jovenes (nombres, telefonos, mails, address, postalZip, region, country, edades)
        case 4:
            print (promediar_edad(edades))


print (menu_estadisticas())
