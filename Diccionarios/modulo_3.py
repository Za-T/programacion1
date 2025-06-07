
def listar_est_ing_inf (datos:list):

    key_list = ["legajo","nombre", "apellido", "edad", "programa"]

    for e_dic in datos:

        if e_dic ["programa"] ["nombre"] == "Ingenieria en Informatica":
            
            for j in range (len(key_list)):
                print (f"{key_list[j]}: {e_dic [key_list[j]]}")

            print ("\n")