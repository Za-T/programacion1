from biblioteca_funciones import *

productos = [ 
{"nombre": "Laptop", "precio": 1200, "categoria": "tecnología"}, 
{"nombre": "Silla", "precio": 150, "categoria": "hogar"}, 
{"nombre": "Smartphone", "precio": 800, "categoria": "tecnología"}, 
{"nombre": "Mesa", "precio": 300, "categoria": "hogar"}, 
{"nombre": "Auriculares", "precio": 200, "categoria": "tecnología"} 
] 

def filtrar_productos (lista_p:list):

    key_list = ["nombre", "precio", "categoria"]

    categoria = input ("Elija categoria (hogar/tecnologia): ")

    for producto in lista_p:
        if producto ["categoria"] == categoria:
            
            
            


#def procesar_productos (lista_p:list, operacion: callable):


filtrar_productos (productos)