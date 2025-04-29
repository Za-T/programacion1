again =  True
repeat_age = True

contador_elite_plano_19_25 = 0

elite_liftado = 0
elite_cortado = 0
elite_plano = 0
saque_elite = " "

nombre_menor = " "
categoria_menor = " "
edad_menor = 0
flag_menor = True

contador_jugadores_avanzado = 0
acumulador_edad_avanzado = 0
promedio_edad_avanzado = 0

contador_jugadores_experto = 0
porcentaje_experto = 0
jugadores_totales = 0

while again == True:

    jugadores_totales += 1

    nombre = input ("\nIngrese nombre de jugador: ")

    edad = int (input ("Ingrese edad: "))

    while repeat_age == True:

        valid_age = input ("Es la edad correcta (S/N)? ")

        if valid_age == "S":
            repeat_age = False

        else:
            edad = int (input ("Ingrese edad: "))


    puntos = int (input ("Ingrese cantidad de puntos: "))
    
    while puntos < 0 or puntos > 60: 
        puntos = int (input ("Error, cantidad de puntos no validos. \nIngrese cantidad de puntos: "))


    victorias = int (input ("Ingrese cantidad de partidos ganados: "))

    while victorias < 0 or victorias > 35:  
        victorias = int (input ("Error, cantidad de victorias no validas. \nIngrese cantidad de partidos ganados: "))


    saque = input ("Ingrese tipo de saque (plano - liftado - cortado): ")
    
    while saque != "plano" and saque != "liftado" and saque != "cortado":
        saque = input ("Error, saque no valido. \nIngrese tipo de saque (plano - liftado - cortado): ")
    
    categoria = input ("Ingrese su categoria (elite - experto - avanzado): ")
    
    while categoria != "elite" and categoria != "experto" and categoria != "avanzado":       
        categoria = input ("Error, cateoria no valida. \nIngrese su categoria (elite - experto - avanzado): ")
    
    match categoria:

        case "elite":
            match saque:

                case "plano":

                    elite_plano += 1

                    if edad >= 19 and edad <= 25:
                        contador_elite_plano_19_25 += 1
            
                case "liftado":
                    elite_liftado += 1

                case "cortado":
                    elite_cortado += 1

        case "avanzado":
            acumulador_edad_avanzado += edad 
            contador_jugadores_avanzado += 1

        case "experto":
            contador_jugadores_experto += 1

    if puntos > 50:
        if flag_menor == True:
            edad_menor = edad
            nombre_menor = nombre
            categoria_menor = categoria
            flag_menor = False

        elif edad < edad_menor :
            edad_menor = edad
            nombre_menor = nombre
            categoria_menor = categoria           

    if again == True :

        valid_again = input ("\nQuiere ingresar otro jugador (S/N): ")

        if valid_again == "N":
            again = False

if elite_cortado > elite_liftado:
    saque_elite = "cortado"
elif elite_liftado > elite_plano:
    saque_elite = "liftado"
else:
    saque_elite = "plano"

if contador_jugadores_avanzado > 0:
    promedio_edad_avanzado = acumulador_edad_avanzado / contador_jugadores_avanzado

porcentaje_experto = (contador_jugadores_experto * 100) / jugadores_totales


print (f"Hay {contador_elite_plano_19_25} jugadores Elite, con saque tipo plano, cuya edad entre 19 y 25 años.")

if edad_menor != 0:
    print (f"El jugador de menor edad con mas de 50 puntos se llama {nombre_menor} y su categoria es {categoria_menor}.")
else:
    print (f"No hay jugador con mas de 50 puntos.")

print (f"El porcentaje de jugadores en categoria experto es del {porcentaje_experto}%")

print (f"El promedio de edad de los jugadores cuya categoría es avanzado es de {promedio_edad_avanzado}")

print (f"El saque más usado por los jugadores cuya categoría es elite es {saque_elite}.")

print ("\nFin del programa.")