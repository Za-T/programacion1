from tablero import *
from preguntas import *
from fun_preguntas import *
from fun_posicion import *
from fun_final import *
from fun_aux import *

def jugar_sye (tablero:list, lista_preguntas:list):

    ''' 
        La fucion jugar_sye se encarga de ejecutar todas las funciones necesesarias para correr el juego.

        Parametros:
            tablero: lista que representa el orden del tablero.
            lista_preguntas: lista de diccionarios que contiene las preguntas y respuestas del juego.
        
    '''
    
    nombre = solicitar_str ("nombre del jugador")

    jugar = continuar_juego (f"¿{nombre}, vas a jugar?")

    posicion = 15

    while jugar == True:

        preguntas = verificar_existencia (lista_preguntas)

        if preguntas == True:

            respuesta_c = mostrar_pregunta (lista_preguntas)

            respuesta_j = validar_str ("\nIngrese su respuesta","a","b","c")

            resultado_res = verificar_igualdad (respuesta_c, respuesta_j, "Correcto!\n", "Incorrecto!\n")
                
            posicion = actualizar_posicion_mov (tablero, posicion, resultado_res)
            
            match posicion:

                case 0:
                    print ("Perdiste.")
                    jugar = False
                
                case 30:
                    print ("Ganaste.")
                    jugar = False
                
                case _:
                    print (f"Tu posicion actual es {posicion}\n")
                    jugar = continuar_juego (f"¿Continuar jugando?")
               
        else:
            print ("\nNo hay mas preguntas.")
            jugar = False
        
    finalizar_juego (nombre, posicion)
        
jugar_sye (tablero, preguntas_c)