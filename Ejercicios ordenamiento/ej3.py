Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria",
               "Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]

Apellidos = ["Sosa", "Gutierrez", "Alsina", "Martinez", "Sosa","Ramirez", "Perez", 
             "Lopez", "Arregui","Mitre", "Andrade", "Loza", "Antares", "Roca", "Perez"]

Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def auxiliar_listas (lista:list,i,j):
    aux = lista [i]
    lista [i] = lista [j]
    lista [j] = aux
    
def ordenar_apellido_asc_nota_des (lista_a: list, lista_nombre: list, lista_nota:list):

    for i in range (len(lista_a)-1):

        for j in range (i+1,len(lista_a)):

            if lista_a [i] > lista_a [j]:

                auxiliar_listas (lista_a, i, j)
                auxiliar_listas (lista_nombre,i, j)
                auxiliar_listas (lista_nota, i,j)

            elif lista_a [i] == lista_a [j]:

                if lista_nombre [i] > lista_nombre [j]:

                    auxiliar_listas (lista_nombre,i, j)
                    auxiliar_listas (lista_nota, i,j)
                
                elif lista_nombre [i] == lista_nombre [j]:

                    if lista_nota [i] < lista_nota [j]:

                        auxiliar_listas (lista_nota, i,j)



