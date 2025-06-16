def escribir_score (ruta:str, nombre:str, puntos: int):

    anotar = [f"Nombre: {nombre}; ",
              f"Puntos: {puntos}; ",
              "\n"]

    with open(ruta, "a") as archivo:
        archivo.writelines(anotar)