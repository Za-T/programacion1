estudiantes = [ 
{"nombre": "Sofía", "curso": "Matemáticas", "calificacion": 7.5}, 
{"nombre": "Tomás", "curso": "Historia", "calificacion": 5.5}, 
{"nombre": "Valentina", "curso": "Ciencias", "calificacion": 9.0}, 
{"nombre": "Lucas", "curso": "Literatura", "calificacion": 4.0}, 
{"nombre": "Martina", "curso": "Física", "calificacion": 6.8} 
]

def mostrar_lista_dic (lista:list):

    for i in range(len(lista)):

        diccionario = lista [i]

        for key, value in diccionario.items():
            print (f"{key}: {value}")
    
        print ("\n")

def filtrar_rango_dic (datos:list, key:str, minimo: float, maximo: float) -> list:

    lista = []

    for dicionario in datos:
        if (dicionario [f"{key}"] >= minimo) and (dicionario [f"{key}"] <= maximo):
            lista.append (dicionario)

    return lista

def mostrar_estudiantes_aprob (datos:list):
    
    aprobados = filtrar_rango_dic (datos, "calificacion", 6, 10)

    mostrar_lista_dic (aprobados)

def procesar_estudiantes (datos:list, operacion: callable) -> callable:

    return operacion (datos)

procesar_estudiantes (estudiantes, mostrar_estudiantes_aprob)