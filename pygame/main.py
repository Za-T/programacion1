from paquete_funciones.validaciones import *
from tablero import *
from preguntas import *
from modulo1 import *
from modulo2 import *
from modulo3 import *
from modulo_extra import *
from csv import *

def jugar_sye (tablero:list, lista_preguntas:list):
    
    nombre = solicitar_str ("nombre del jugador")

    jugar = continuar_juego (f"¿{nombre}, vas a jugar?")

    posicion = 15

    while jugar == True:

        preguntas = verificar_existencia (lista_preguntas)

        if preguntas == True:

            respuesta_c = mostrar_pregunta (lista_preguntas)

            respuesta_j = validar_str ("la respuesta correcta","a","b","c")

            resultado_res = verificar_igualdad (respuesta_c, respuesta_j, "Correcto!", "Incorrecto!")
                
            posicion = calcular_posicion (tablero, posicion, resultado_res)
            
            if posicion != 0 and posicion != 30:

                print (f"Tu posicion actual es {posicion}")
                jugar = continuar_juego (f"¿Continuar jugando?")

            elif posicion == 0:

                print ("Perdiste.")
                jugar = False

            elif posicion == 30:
                
                print ("Ganaste.")
                jugar = False

        else:
            print ("No hay mas preguntas.\n")
            jugar = False
        
        if jugar == False:
            print (f"Fin del juego.\n"
                f"{nombre} llego a la posicion {posicion}.")
            escribir_score("Score.csv", nombre, posicion)
        

jugar_sye (tablero, preguntas_c)