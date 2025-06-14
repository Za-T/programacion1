import json

def leer_json (direccion:str ,nombre_lista:str):

    try:
        
        with open(direccion, "r+") as archivo :
            datos_archivo = json.load(archivo)
        archivo.close()

        if nombre_lista in datos_archivo:
            for heroe in datos_archivo[nombre_lista]:
                for esp in heroe:
                    print (f"{esp}: {heroe[esp]}")
                print ("\n")

    except FileNotFoundError:
        print ("Ese archivo no existe.")
