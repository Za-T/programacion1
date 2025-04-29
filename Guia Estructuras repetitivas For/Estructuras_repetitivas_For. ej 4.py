multiplicador = int (input ("Ingrese multiplicador : "))
multiplicando = 0
producto = 0
flag = True


for i in range (11):
   if flag == True:
     print (f"{multiplicador} * {multiplicando} = {producto}")
     flag = False

   else:
     multiplicando += 1
     producto = multiplicador * multiplicando
     print (f"{multiplicador} x {multiplicando} = {producto}") 

print ("Fin del programa.")