def realizar_descuento (valor:int, descuento = 5) -> int:
    descuento_total = (valor * descuento) / 100
    return valor - descuento_total

def validar (num: int) -> int:
    
    while num < 10 or num > 100:
        num = int (input ("Error, valor invalido. Ingrese un nuevo valor: ")) 
    
    return num
       
numero1 = int (input ("Ingrese un valor: "))

numero1 = validar (numero1)

print ("El valor una vez aplicado el descuento es", realizar_descuento (numero1))