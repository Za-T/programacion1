def escribir_score (ruta:str, nombre:str, puntos: int):

    anotar = [f"Nombre: {nombre}; ",
              f"Puntos: {puntos}; "]

    with open(ruta, "r+") as archivo:
        archivo.writelines(anotar)