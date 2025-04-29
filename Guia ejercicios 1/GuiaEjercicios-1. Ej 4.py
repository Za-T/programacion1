edad = int (input("Ingrese edad: "))
est_civ = (input ("Ingrese estado civil: "))

while edad < 18 and est_civ != "soltero": 
    print ("Usted es muy joven para no ser soltero. Vuelva a ingresar los datos.")
    edad = int (input("Ingrese edad: "))
    est_civ = (input ("Ingrese estado civil: "))

print ("Datos ingresados.")