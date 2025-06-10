from biblioteca_funciones import *

def listar_club (datos: list):
    
    key_list = ["promedio", "nombre", "apellido", "grupos"]

    for e_dic in datos:

        if "grupos" in e_dic:

            for grupo in e_dic ["grupos"]:

                if grupo ["nombre"] == "Club de Informatica":

                    try:
                        for j in range (len(key_list)):
                            print (f"{key_list[j]}: {e_dic [key_list[j]]}")

                    except KeyError:
                        promediar_notas (datos)

                        for j in range (len(key_list)):
                            print (f"{key_list[j]}: {e_dic [key_list[j]]}")

            print ("\n")