print ("-------------------------------------")

tipo_cliente = input ("Tipo de cliente: ")

print (" ")

cant_mc = float  (input ("Cantidad de metros cosumidos: "))

print ("-------------------------------------")

print (" ")

CARGO_FIJO = 7000
subtotal = CARGO_FIJO + (cant_mc * 200)
bonificacion = 0
recargo = 0
subtotal_rec_bon = 0
iva = 0.21
precio_final = 0

match tipo_cliente:
    case "Residencial" :
        if cant_mc < 30 :
            bonificacion = 10
        elif cant_mc > 80 :
            recargo = 15
           
    case "Comercial" :
        if cant_mc < 50 :
            bonificacion = 5
        elif cant_mc > 150 and cant_mc <= 300:
            bonificacion = 8
        elif cant_mc < 300:
            bonificacion = 12
    
    case "Industrial" :
        if cant_mc < 200:
            recargo = 10
        elif cant_mc > 500 and cant_mc <= 1000:
            bonificacion = 20
        elif cant_mc > 1000 : 
            bonificacion = 30

    case _: 
        print ("Datos no validos.")

if tipo_cliente == "Residencial" and subtotal < 35000:
    bonificacion += 5

bonificacion = (bonificacion * subtotal) / 100
recargo = (recargo * subtotal) / 100

subtotal_rec_bon = subtotal - bonificacion + recargo

iva *= subtotal_rec_bon

precio_final = subtotal_rec_bon + iva 
            



print (" ")

print ("-------------------------------------")

print (" ")

print ("El subtotal es de: $", subtotal)

print (" ")

print ("Las bonificaciones son de: $", bonificacion)

print (" ")

print ("Los recargos son de: $", recargo)

print (" ")

print ("-------------------------------------")

print (" ")

print ("El subtotal, con recargos y bonificaciones es de: $", subtotal_rec_bon)

print (" ")

print ("El IVA es de: $", iva)

print (" ")

print ("-------------------------------------")

print (" ")

print ("El valor total a pagar es de: $", precio_final)

print (" ")