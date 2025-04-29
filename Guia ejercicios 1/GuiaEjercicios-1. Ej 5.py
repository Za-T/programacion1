estacion = input ("Ingrese estacion del año: ")
localidad = input ("Ingrese localidad a viajar: ")

precio_base = 15000
precio_final = 0

match localidad:
    case "Bariloche":
        if estacion == "Invierno":
            precio_final = precio_base * 1.20
        elif estacion == "Verano":
            precio_final = precio_base * 0.80
        else:
            precio_final = precio_base * 1.10

    case "Cataratas":
        if estacion == "Invierno":
            precio_final = precio_base * 0.90
        elif estacion == "Verano":
            precio_final = precio_base * 1.10
        else:
            precio_final = precio_base * 1.10

    case "Mar del Plata":
        if estacion == "Invierno":
            precio_final = precio_base * 0.80
        elif estacion == "Verano":
            precio_final = precio_base * 1.20
        else:
            precio_final = precio_base * 1.10

    case "Cordoba":
        if estacion == "Invierno":
            precio_final = precio_base * 0.90
        elif estacion == "Verano":
            precio_final = precio_base * 1.10
        else:
            precio_final = precio_base
    
    case _:
        print ("Datos no validos.")

print (" ")
print ("El precio final es: $", precio_final)