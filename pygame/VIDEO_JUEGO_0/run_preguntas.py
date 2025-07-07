import pygame
from copy import deepcopy
from modulo_aux import *
from constantes_main import *
from tablero import *
import random

def mostrar_pregunta (screen, pregunta, fuente, color):
    
    pregunta_elegida = pregunta["pregunta"]
    respuesta_a = pregunta["respuesta_a"]
    respuesta_b = pregunta["respuesta_b"]
    respuesta_c = pregunta["respuesta_c"]

    txt_pregunta = fuente.render(str(pregunta_elegida), True, color)
    txt_respuesta_a = fuente.render(str(respuesta_a), True, color)
    txt_respuesta_b = fuente.render(str(respuesta_b), True, color)
    txt_respuesta_c = fuente.render(str(respuesta_c), True, color)

    screen.blit(txt_pregunta,(x_pregunta, y_pregunta))
    screen.blit(txt_respuesta_a,(x_izq, y))
    screen.blit(txt_respuesta_b,(x_medio, y))
    screen.blit(txt_respuesta_c,(x_der, y))
 
def obtener_respuesta_j (evento, lista_posicion:list)->str:

    retorno = None

    if evento.type == pygame.MOUSEBUTTONDOWN:

        if rect_a.collidepoint(lista_posicion):
            retorno = "a"
        elif rect_b.collidepoint(lista_posicion):
            retorno = "b"
        elif rect_c.collidepoint(lista_posicion):
            retorno = "c"
    
    return retorno
                
def calcular_posicion (respuesta_c, respuesta_j, posicion_j:int, tablero: list, screen, fuente):
    
    mensaje = None 

    if posicion_j != 0 and posicion_j != 30:
       
        if respuesta_j == respuesta_c: #respuesta correcta

            posicion_j += 1

            if tablero [posicion_j] != 0:
                mensaje = f"Caiste en escalera, adelantas {tablero [posicion_j]} casilleros."
                posicion_j += tablero [posicion_j]

        else:
            posicion_j -= 1
            if tablero [posicion_j] != 0:            
                mensaje = f"Caiste en serpiente, regresas {tablero [posicion_j]} casilleros."
                posicion_j -= tablero [posicion_j]

        txt_mensaje = fuente.render(str(mensaje), True, BLACK)

        pygame.draw.rect(screen, WHITE, rect_resultado)
        screen.blit(txt_mensaje,(x_pregunta, y_pregunta))

#def dibujar_posicion ():

def manejar_tablero (screen, preguntas_c, tablero, reloj, gestion_tablero:list, fuente, evento, lista_posicion: list):
    
    "La funcion maneja el tablero. Primero elige una pregunta random, una vez que la tiene, empieza un timer, d"
    "Se muestra la pregunta elegida, y las opciones para contestar, "
    "si coliciona con el rectangulo correcto avanza la posicion del tablero, "
    "si es con el incorrecto vuelve para atras"
    "En caso de que el timer (20 seg) se acaba y no hubo una colision, se toma como respuesta incorrecta"

    atribuir_fondo ("imagenes/tablero.png",screen)
    posicion_j = gestion_tablero [2]

    if evento.type == pygame.MOUSEBUTTONDOWN:
        if rect_tablero_salir.collidepoint(lista_posicion):
            gestion_tablero [0] = False

    existencia = verificar_existencia (preguntas_c)

    if existencia == True and gestion_tablero[0] == True:

        if gestion_tablero [1] == None: #si no hay pregunta, elegirla
            pregunta = random.choice(preguntas_c)
            gestion_tablero [1] = pregunta

        else: #hay pregunta elegida
            pregunta = gestion_tablero [1]
            timer_event = pygame.USEREVENT + 1 #configurar timer
            pygame.time.set_timer(timer_event, 1000)

            mostrar_pregunta (screen, pregunta, fuente, BLACK) #solo imprime la pregunta durante lo que dure el timer, o hasta que haya una colicion

            respuesta_c = gestion_tablero [1] ["respuesta_correcta"]
            respuesta_j = obtener_respuesta_j(evento, lista_posicion) 

            if respuesta_j != None:
                posicion_j = calcular_posicion (respuesta_c, respuesta_j, posicion_j, tablero, screen, fuente)

    else:
        gestion_tablero [0] = False #si no hya mas preguntas, terminar juego

    return gestion_tablero        
    
