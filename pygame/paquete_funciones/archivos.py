def leer_json (direccion:str ,nombre_lista:str):

    import json
    
    try:
        
        with open(direccion, "r+") as archivo :
            datos_archivo = json.load(archivo)
        archivo.close()

        if nombre_lista in datos_archivo:
            for item in datos_archivo[nombre_lista]:
                for esp in item:
                    print (f"{esp}: {item[esp]}")
                print ("\n")

        return datos_archivo

    except FileNotFoundError:
        print ("Ese archivo no existe.")