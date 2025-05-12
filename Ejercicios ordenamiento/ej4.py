from listas_personas import *
from biblioteca_funciones import *


def mostrar_datos_mexico (nombres: list, telefonos:list, mail:list,adress:list,postalzip:list,region:list,country:list,edades:list):

    '''Muestra los datos de los usuarios de México '''

    for i in range (len(country)):

        if country [i] == "Mexico":

            print (f"Nombre: {nombres[i]}\nTelefono:{ telefonos [i]}\nMail:{ mail [i]}\nDireccion: {adress [i]}\nCodigo Postal: {postalZip [i]}\nRegion: {region [i]}\nPais: {country [i]}\nEdad: {edades [i]}\n")

def mostrar_datos_brazil  (nombres: list, telefonos:list, mail:list,country:list):
    
    '''Muestra el nombre, mail y teléfono de todos los usuarios de Brazil'''

    for i in range (len(country)):
        if country [i] == "Brazil":
            print (f"Nombre: {nombres[i]}\nTelefono:{ telefonos [i]}\nMail:{ mail [i]}\n")

def mostrar_datos_jovenes (nombres: list, telefonos:list, mail:list,adress:list,postalzip:list,region:list,country:list,edades:list):

    '''Muestra los datos de los usuarios mas jovenes'''

    edad_menor = edades [0]

    for i in range (len(edades)):

        if edades [i] <= edad_menor:
            print (f"Nombre: {nombres[i]}\nTelefono:{ telefonos [i]}\nMail:{ mail [i]}\nDireccion: {adress [i]}\nCodigo Postal: {postalZip [i]}\nRegion: {region [i]}\nPais: {country [i]}\nEdad: {edades [i]}\n")

def promediar_edad (edades:list) ->int:

    '''Promedia la edad de todos los usuarios'''

    suma_edades = 0
    total_edades = 0

    for i in range (len(edades)) :

        suma_edades += edades [i]
        total_edades += 1

    promedio_edades = suma_edades // total_edades

    return promedio_edades

def mostrar_mayor_datos_brazil (nombres: list, telefonos:list, mail:list,adress:list,postalzip:list,region:list,country:list,edades:list):

    '''Muestra los datos del usuario de mayor edad de Brazil'''

    edades_brazil = [0] * len(edades)

    flag = True

    for i in range (len(country)):

        if country [i] == "Brazil":

            if flag == True:

                edad_mayor = edades [i]

                flag = False

            if edades [i] >= edad_mayor:

                print (f"Nombre: {nombres[i]}\nTelefono:{ telefonos [i]}\nMail:{ mail [i]}\nDireccion: {adress [i]}\nCodigo Postal: {postalZip [i]}\nRegion: {region [i]}\nPais: {country [i]}\nEdad: {edades [i]}\n")

def mostrar_mxc_brz_codpos_8000 (nombres: list, telefonos:list, mail:list,adress:list,postalzip:list,region:list,country:list,edades:list):

    '''Muestra  los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 '''

    for i in range (len(postalZip)):

        if postalZip [i] >= 8000:

            if country [i] == "Brazil" or country [i] == "Mexico":

                print (f"Nombre: {nombres[i]}\nTelefono:{ telefonos [i]}\nMail:{ mail [i]}\nDireccion: {adress [i]}\nCodigo Postal: {postalZip [i]}\nRegion: {region [i]}\nPais: {country [i]}\nEdad: {edades [i]}\n")

def mostrar_italianos_mayores_40 (nombres: list, telefonos:list, mail:list,country:list,edades:list):

    '''Muestra el nombre, mail y teléfono de los usuarios italianos mayores a 40 años. '''

    for i in range(len(country)):

        if country == "Italy":

            if buscar_mayor_lista (edades) >= 40:

                print (f"Nombre: {nombres[i]}\nTelefono:{ telefonos [i]}\nMail:{ mail [i]}\n")
     

def seleccionar_menu_estadisticas ():

    '''Permite seleccionar que estadistica se quiere ver, y da la opcion de seleccionar otra al final'''

    repetir = "s"

    while repetir == "s":

        print ("Menu de Opciones:" \
        "\n1.Lista de los datos de los usuarios de México." \
        "\n2.Listar los nombre, mail y teléfono de los usuarios de Brasil." \
        "\n3.Listar los datos del/los usuario/s más joven/es." \
        "\n4.Obtener un promedio de edad de los usuarios." \
        "\n5.De los usuarios de Brasil, listar los datos del usuario de mayor edad." \
        "\n6.Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000." \
        "\n7.Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.\n")

        opcion = validar_int("opcion",1,7)

        match opcion:
            case 1:
                mostrar_datos_mexico(nombres, telefonos, mails, address, postalZip, region, country, edades)
            case 2:
                mostrar_datos_brazil (nombres, telefonos, mails, country)
            case 3:
                mostrar_datos_jovenes (nombres, telefonos, mails, address, postalZip, region, country, edades)
            case 4:
                print (promediar_edad(edades))
            case 5:
                mostrar_mayor_datos_brazil (nombres, telefonos, mails, address, postalZip, region, country, edades)
            case 6:
                mostrar_mxc_brz_codpos_8000 (nombres, telefonos, mails, address, postalZip, region, country, edades)
            case 7:
                mostrar_italianos_mayores_40 (nombres, telefonos, mails, country, edades)

        repetir = validar_str ("si quiere solicitar otra opcion", "s", "n")

seleccionar_menu_estadisticas()