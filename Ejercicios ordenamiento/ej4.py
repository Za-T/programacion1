from listas_personas import *
from biblioteca_funciones import *

def auxiliar_listas (lista:list,i,j):
    aux = lista [i]
    lista [i] = lista [j]
    lista [j] = aux


def mostrar_datos_mexico (nombres: list, telefonos:list, mail:list,adress:list,postalzip:list,region:list,country:list,edades:list):

    '''Muestra los datos de los usuarios de México '''

    for i in range (len(country)):

        if country [i] == "Mexico":

            print (f"Nombre: {nombres[i]}\nTelefono:{ telefonos [i]}\nMail:{ mail [i]}\nDireccion: {adress [i]}\nCodigo Postal: {postalzip [i]}\nRegion: {region [i]}\nPais: {country [i]}\nEdad: {edades [i]}\n")

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
            print (f"Nombre: {nombres[i]}\nTelefono:{ telefonos [i]}\nMail:{ mail [i]}\nDireccion: {adress [i]}\nCodigo Postal: {postalzip [i]}\nRegion: {region [i]}\nPais: {country [i]}\nEdad: {edades [i]}\n")

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

                print (f"Nombre: {nombres[i]}\nTelefono:{ telefonos [i]}\nMail:{ mail [i]}\nDireccion: {adress [i]}\nCodigo Postal: {postalzip [i]}\nRegion: {region [i]}\nPais: {country [i]}\nEdad: {edades [i]}\n")

def mostrar_mxc_brz_codpos_8000 (nombres: list, telefonos:list, mail:list,adress:list,postalzip:list,region:list,country:list,edades:list):

    '''Muestra  los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 '''

    for i in range (len(postalzip)):

        if postalzip [i] >= 8000:

            if country [i] == "Brazil" or country [i] == "Mexico":

                print (f"Nombre: {nombres[i]}\nTelefono:{ telefonos [i]}\nMail:{ mail [i]}\nDireccion: {adress [i]}\nCodigo Postal: {postalzip [i]}\nRegion: {region [i]}\nPais: {country [i]}\nEdad: {edades [i]}\n")

def mostrar_italianos_mayores_40 (nombres: list, telefonos:list, mail:list,country:list,edades:list):

    '''Muestra el nombre, mail y teléfono de los usuarios italianos mayores a 40 años. '''

    for i in range(len(country)):

        if country == "Italy":

            if buscar_mayor_lista (edades) >= 40:

                print (f"Nombre: {nombres[i]}\nTelefono:{ telefonos [i]}\nMail:{ mail [i]}\n")
     
def mostrar_mxc_ordenado_nombre (nombres: list, telefonos:list, mail:list,adress:list,postalzip:list,region:list,country:list,edades:list):

    for i in range (len (country)-1):

        if country [i] == "Mexico":

            for j in range (i+1, len(nombres)):

                if nombres[i] > nombres[j]:

                    auxiliar_listas(telefonos, i, j)
                    auxiliar_listas(mail, i, j)
                    auxiliar_listas(adress, i, j)
                    auxiliar_listas(postalzip, i, j)
                    auxiliar_listas(region, i, j)
                    auxiliar_listas(edades, i, j)
       
            #no funciona para el primer sort

            print(f"Nombre: {nombres[i]}\nTelefono:{ telefonos [i]}\nMail:{ mail [i]}\nDireccion: {adress [i]}\nCodigo Postal: {postalzip [i]}\nRegion: {region [i]}\nPais: {country [i]}\nEdad: {edades [i]}\n")

def mostrar_datos_joven_asc (nombres: list, telefonos:list, mail:list,adress:list,postalzip:list,region:list,country:list,edades:list):

    flag = True

    for i in range (len(edades)-1):

        if flag == True:
           edad_menor = edades [i]
           flag = False
        
    



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

        opcion = validar_int("opcion",1,10)

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
            case 8:
                mostrar_mxc_ordenado_nombre (nombres, telefonos, mails, address, postalZip, region, country, edades)
            case 9:
                mostrar_datos_joven_asc ()


        repetir = validar_str ("si quiere solicitar otra opcion", "s", "n")

seleccionar_menu_estadisticas()