from modulo1 import *

datos_archivo = leer_json ("data_stark.json", "heroes")

def generar_csv (ruta:str, lista_s:list):
    
    archivo = open(ruta, "w")

    for heroe in lista_s:
        for esp in heroe:        
                archivo.write (f"{esp}: {heroe[esp]}")
                archivo.write ("\n")
        archivo.write ("\n")
    
    archivo.close

generar_csv ("heroes.csv", datos_archivo["heroes"])