'''
  "title": "QUEVEDO || BZRP Music Sessions #52",
  "views": 227192970,
  "length": 204,
  "img_url": "https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg",
  "url": "https://youtube.com/watch?v=A_g3lMcWVy0",
  "date":
'''
#CONVERTIR LOS DATOS A MEMORIA EN UNA LISTA DE DICCIONARIOS
#GENERAR UN ARCHIVO CSV

def parse_csv(nombre_archivo:str)->list:
    lista_rta = []
    archivo = open(nombre_archivo, "r")
    for e_linea in archivo:
        lista_temp = e_linea.split(",")
        #crear el diccionario
        tema = {}
        tema["title"] = lista_temp[0]
        tema["views"] = lista_temp[1]
        tema["length"] = lista_temp[2]
        tema["img_url"] = lista_temp[3]
        tema["url"] = lista_temp[4]
        tema["date"] = lista_temp[5]
        lista_rta.append(tema)
    archivo.close()
    return lista_rta


def generar_csv(nombre_archivo:str, lista:list):
    with open(nombre_archivo,"w") as archvio:
        for e_tema in lista:
            linea = "{0},{1},{2},{3},{4},{5}"
            linea = linea.format(
                                e_tema["title"],
                                e_tema["views"],
                                e_tema["length"],
                                e_tema["img_url"],
                                e_tema["url"],
                                e_tema["date"])  
            #print(linea)
            archvio.write(linea)


lista = parse_csv("data.csv")
print(lista[0])
generar_csv("data_salida.csv", lista)
