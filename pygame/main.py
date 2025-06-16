from paquete_funciones.validaciones import *
from tablero import *
from preguntas import *
from modulo1 import *
from modulo2 import *
from modulo_extra import *

def jugar_sye (tablero:list, lista_preguntas:list):
    
    nombre = solicitar_str ("nombre del jugador")

    jugar = continuar_juego (f"¿{nombre}, vas a jugar?")

    posicion = 15

    while jugar == True:

        respuesta_c = mostrar_pregunta (lista_preguntas)

        respuesta_j = validar_str ("la respuesta correcta","a","b",",c")

        resultado_res = verificar_igualdad (respuesta_c, respuesta_j, "Correcto!", "Incorrecto!")
            
        posicion = calcular_posicion (tablero, posicion, resultado_res)
        
        if posicion == int:

            jugar = continuar_juego (f"si seguir jugando")

    if jugar == False:
        print (f"{nombre} llego a la posicion {posicion}")

jugar_sye (tablero, preguntas_c)