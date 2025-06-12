'''
  "title": "QUEVEDO || BZRP Music Sessions #52",
  "views": 227192970,
  "length": 204,
  "img_url": "https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg",
  "url": "https://youtube.com/watch?v=A_g3lMcWVy0",
  "date":
'''
#LECTURA DE UN ARCHIVO

def parse_csv(nombre_archivo:str)->list:
    lista = []
    #archivo = open(nombre_archivo,"r")
    with open(nombre_archivo, "r") as archivo:
      for e_linea in archivo:
          lista.append(e_linea)
      #archivo.close()
    return lista

lista = []
lista = parse_csv("data.csv")
print(lista[0])