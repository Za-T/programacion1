from biblioteca_funciones import *

productos = [ 
{"nombre": "Laptop", "precio": 1200, "categoria": "tecnología"}, 
{"nombre": "Silla", "precio": 150, "categoria": "hogar"}, 
{"nombre": "Smartphone", "precio": 800, "categoria": "tecnología"}, 
{"nombre": "Mesa", "precio": 300, "categoria": "hogar"}, 
{"nombre": "Auriculares", "precio": 200, "categoria": "tecnología"} 
] 

def mostrar_producto (producto):
        for key in producto:
            print (f"{key}: {producto[key]}")
        print ("\n")

def filtrar_productos (lista_p:list, categoria):
    for producto in lista_p:
        if producto ["categoria"] == categoria:
            mostrar_producto (producto)

def correr_op_1 (lista_p:list) -> callable:
    
    categoria = validar_str ("categoria","hogar","tecnologia")  

    return filtrar_productos (lista_p, categoria)
                  
def promediar_num_dic (lista_n: list, key: str) -> int:
    
    suma = 0
    cant_total = len(lista_n)

    for valor in lista_n:
        suma += valor [f"{key}"]
    
    promedio = suma / cant_total
    return promedio

def correr_op_2 (lista_p:list):
     
    try: 
        print (promediar_num_dic (productos, "precio"))

    except ZeroDivisionError:
        print("Error: No se puede calcular el promedio de una lista vacía")
    
def procesar_productos (lista_p:list, operacion: callable):
    operacion (lista_p)

procesar_productos (productos, correr_op_2)