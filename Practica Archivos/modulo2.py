from modulo1 import *

datos_archivo = leer_json ("data_stark.json", "heroes")

def generar_csv (ruta:str, lista_s:list):
    
    archivo = open(ruta, "w")

    for dic in lista_s:
            for heroe in dic:
                archivo.write (f"{lista_s[dic][heroe]}")
                archivo.write ("\n")

    archivo.close

generar_csv ("heroes.csv", datos_archivo)