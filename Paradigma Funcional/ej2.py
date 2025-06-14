estudiantes = [ 
{"nombre": "Sofía", "curso": "Matemáticas", "calificacion": 7.5}, 
{"nombre": "Tomás", "curso": "Historia", "calificacion": 5.5}, 
{"nombre": "Valentina", "curso": "Ciencias", "calificacion": 9.0}, 
{"nombre": "Lucas", "curso": "Literatura", "calificacion": 4.0}, 
{"nombre": "Martina", "curso": "Física", "calificacion": 6.8} 
]

from biblioteca_funciones import *

def filtrar_rango_dic (datos:list, key:str, minimo: float, maximo: float) -> list:

    lista = []

    for elemento in datos:
        if (elemento [f"{key}"] >= minimo) and (elemento [f"{key}"] <= maximo):
            lista.append (elemento)

    return lista


def mostrar_est_aprob (datos:list):
    
    aprobados = filtrar_rango_dic (datos, "calificacion", 6, 10)

    mostrar_lista (aprobados)


def procesar_estudiantes (datos:list, operacion: callable) -> callable:

    return operacion (datos)

procesar_estudiantes (estudiantes, mostrar_est_aprob)