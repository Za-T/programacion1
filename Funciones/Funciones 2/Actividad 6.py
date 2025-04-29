def calculador_potencia (base:int, exponente: int) -> int:

    '''Calcula la potencia de un numero, segun la base y exponente pedidos'''

    potencia = base ** exponente
    return f" {base} elevado a {exponente} es igual a {potencia}"

print (calculador_potencia(4,0))