def sumar_naturales (numero:int) -> int:

    if numero == 9:
        return 9
    
    else:
        return numero + sumar_naturales (numero+1)

      
print (sumar_naturales (1))
