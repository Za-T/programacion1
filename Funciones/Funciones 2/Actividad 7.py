from Biblioteca_de_Funciones import * 


def identificador_primos (numero:int,divisor:int) -> bool :
    
    flag = True

    if divisor == 1:
        flag = True 
        return flag
    elif numero % divisor == 0:
        flag = False
        return flag
    else:
        return identificador_primos (numero, divisor-1) #pq si no pongo el return en cada uno, el resultado es none

    #return flag #pq eso esta mal?

numero = solicitar_entero ("numero")

divisor = numero - 1

print (identificador_primos (numero,divisor)) 