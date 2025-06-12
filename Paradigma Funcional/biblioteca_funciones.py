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

    cadena = input (f"Ingrese {valor} ({op1},{op2}): ")

    while cadena != op1 and cadena != op2:
        cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2}): "))
    
    return cadena

def solicitar_str (nombre_valor: str) -> str:
    '''Solicita al usuario el ingreso de una cadena y la retorna'''
    cadena = str (input (f"Ingresar {nombre_valor}: "))
    return cadena

def buscar_mayor_lista (lista_num:list) -> int:

    '''Busca y retorna el mayor valor dentro de una lista'''

    flag = True

    for i in range (len(lista_num)):

        if flag == True:

                edad_mayor = lista_num [i]

                flag = False

        if lista_num [i] >= edad_mayor:
             
            edad_mayor = lista_num [i]

    return edad_mayor

def buscar_menor_lista (lista_num:list) -> int:

    '''Busca y retorna el menor valor dentro de una lista'''

    flag = True

    for i in range (len(lista_num)):

        if flag == True:

                edad_menor = lista_num [i]

                flag = False

        if lista_num [i] <= edad_menor:
             
            edad_menor = lista_num [i]

    return edad_menor

def ordenar_lista_ascendente (lista:list) -> list:
 
    for i in range(len(lista)-1):
        for j in range (i+1,len(lista)):
            if (lista [i] > lista[j]):
                aux = lista [i]
                lista [i] = lista [j]
                lista [j] = aux
    
    return lista 

def auxiliar_listas (lista:list,i,j):
    aux = lista [i]
    lista [i] = lista [j]
    lista [j] = aux

def auxiliar_listas_dic (lista:list, clave:str, i:int,j:int):
    aux = lista [i] [clave]
    lista [i] [clave] = lista [j] [clave]
    lista [j] [clave] = aux

def mostrar_keys (datos:list,key_list:list):

    for i in range(len(datos)):
        for j in range (len(key_list)):
            print (f"{key_list[j]}: {datos[i][key_list[j]]}")
        print ("\n")

def mostrar_lista (lista:list):

    for i in range(len(lista)):
        print (f"\n{lista[i]}")

def promediar_item (datos, key) -> int:
    
    suma_value = 0

    #por cada elemento de la lista
    for e_dic in datos:
        suma_value += e_dic[f"{key}"]

    cant = len(datos)
    promedio = suma_value // cant

    return promedio

def promediar_notas (datos:list):

    #por cada elemento de la lista
    for i in range (len(datos)):

        suma_notas = 0

        #por cada nota
        for j in range (len(datos [i]["notas"])):
            suma_notas += datos[i]["notas"][j]

        cant_notas = len(datos [i]["notas"])

        promedio = suma_notas // cant_notas

        datos [i]["promedio"] = promedio

def promediar_num_dic (lista_n: list, key: str) -> int:
    
    suma = 0
    cant_total = len(lista_n)

    for valor in lista_n:
        suma += valor [f"{key}"]
    
    promedio = suma / cant_total
    return promedio

def asignar_valores (valor) -> dict:

    datos_dic = {
        "legajo" : valor ["legajo"],
        "nombre" : valor ["nombre"],
        "apellido" : valor ["apellido"],
        "programa" : valor ["programa"],
    }

    return datos_dic

