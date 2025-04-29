iot_ia_m_25_50 = 0
not_ia_not_f_not_33_40 = 0
porcentaje = 0
mayor_edad_masc = 0
total_empleados = 10
flag = True

for i in range (total_empleados):

    nombre = input ("Ingrese nombre del empleado: ")

    edad = int (input ("Ingrese edad: "))
    while edad < 18:
        edad = int (input ("Error. Ingrese edad no menor a 18: "))

    genero = input ("Ingrese genero (M - F - X): ")

    tecnologia = input ("Ingrese tecnologia (IA, RV/RA, IOT): ")

    if genero == "M":
        
        if flag == True:
            mayor_edad_masc = edad
            tecnologia_mayor = tecnologia
            nombre_mayor = nombre
            flag = False

        elif edad > mayor_edad_masc:
            mayor_edad_masc = edad
            tecnologia_mayor = tecnologia
            nombre_mayor = nombre
        
        if tecnologia == "IA" or tecnologia == "IOT" and edad >= 25 and edad <= 50:
            iot_ia_m_25_50 += 1

    if tecnologia != "IA":
        if genero != "F" or (edad < 33  or  edad > 40 ):       
            not_ia_not_f_not_33_40 += 1
    

porcentaje = (not_ia_not_f_not_33_40 * 100) / total_empleados 

print ("La cantidad de empleados de genero masculino que que votaron por IOT o IA, cuya edad esté entre 25 y 50 años es de:", iot_ia_m_25_50)

print (f"Porcentaje de empleados que no votaron por IA, cuyo género no sea Femenino o su edad se encuentre entre los 33 y 40: {porcentaje}%") 

if flag == False:

    print (f"Los nombres de los empleados masculinos de mayor edad son: {nombre_mayor}. \n La tecnologia que votaron fue: {tecnologia_mayor}.")