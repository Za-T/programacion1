import json

def leer_json (direccion:str ,nombre_lista:str):

    try:
        
        with open(direccion, "r+") as archivo :
            datos_archivo = json.load(archivo)
        archivo.close()

        return datos_archivo

    except FileNotFoundError:
        print ("Ese archivo no existe.")
