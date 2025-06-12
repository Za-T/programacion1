
def recorrer_columnas (matriz:list):
    #columna
    for i in range(len(matriz[0])):
        #fila
        for j in range(len(matriz)-2):
        
            if matriz[j][i] == matriz[j+1][i] == matriz[j+2][i]:
                print (f"El numero {matriz[j][i]} esta repetido")

matriz = [
        [5, 2, 7, 2],
        [5, 2, 7, 4],
        [5, 2, 3, 4],
        [1, 6, 7, 4]
        ]

recorrer_columnas (matriz)

