edad = int (input ("Escriba su edad: "))

if edad <= 0 or edad > 120:
    print ("Edad no valida.")
elif edad < 13:
    print ("Usted es menor.")
elif edad < 18:
    print ("Usted es adolescente.")
else:
    print ("Usted es mayor de edad.")