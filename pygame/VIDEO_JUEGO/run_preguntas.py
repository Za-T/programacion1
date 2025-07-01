import pygame
from copy import deepcopy
from modulo_aux import *
import random

def manejar_tablero (preguntas_c, dict_rect, screen, evento, lista_posicion, gestionar_preguntas, FUENTE, COLOR_PREGUNTAS,):

    atribuir_fondo ("imagenes/tablero.png",screen)

    existencia = verificar_existencia (preguntas_c)

    respuesta_correcta = None

    if existencia == True:

        if gestionar_preguntas [1] == None: #no hay pregunta elegida

            pregunta = random.choice(preguntas_c) # Variable local temporal

            timer_segundos = pygame.USEREVENT + 1
            pygame.time.set_timer(timer_segundos, 45000)

            respuesta_correcta = mostrar_preguntas(pregunta, screen, FUENTE, COLOR_PREGUNTAS)
            gestionar_preguntas [1] = pregunta # Guarda la pregunta actual
            gestionar_preguntas[3] = respuesta_correcta # Guarda la respuesta correcta

        else: # Si ya hay una pregunta activa

            # Renderizar la pregunta activa en cada frame
            mostrar_preguntas(gestionar_preguntas[1], screen, FUENTE, COLOR_PREGUNTAS)

            if gestionar_preguntas [2] == None:
                lista_rect_correcto = asignar_rectangulo_correcto (dict_rect, gestionar_preguntas[3])
                resultado_ronda = verificar_respuesta (evento, lista_posicion, lista_rect_correcto)

                if resultado_ronda != None:
                    gestionar_preguntas [2] = True

            if resultado_ronda  != None:

                if resultado_ronda == True:
                    print ("Correcto!")
                elif resultado_ronda == False:
                    print ("Incorrecto!")

                preguntas_c.remove(gestionar_preguntas[1]) # Eliminamos la pregunta actual (usando gestionar_preguntas[1])

                #resetear flags
                gestionar_preguntas[1] = None
                gestionar_preguntas[2] = None
                gestionar_preguntas[3] = None
            
    else:
        gestionar_preguntas[0] = False #dejar de correr

    return gestionar_preguntas 

def asignar_rectangulo_correcto (dict_rectangulo, respuesta_correcta) -> list:

    rect_correcto = dict_rectangulo[respuesta_correcta]
    rect_incorrecto1 = None
    rect_incorrecto2 = None

    for key in dict_rectangulo:
        if key != respuesta_correcta:
            if rect_incorrecto1 == None:
                rect_incorrecto1 = dict_rectangulo [key]
            else:
                rect_incorrecto2 = dict_rectangulo [key]

    lista_rectangulo = [rect_correcto, rect_incorrecto1, rect_incorrecto2]

    return lista_rectangulo

def mostrar_preguntas (pregunta, screen, fuente, color) -> str:

    x_pregunta = 150.2
    y_preguntas = 41.3
    x_izq = 70
    x_medio = 390
    x_der = 695
    y = 127.5
    
    pregunta_elegida = pregunta["pregunta"]
    respuesta_a = pregunta["respuesta_a"]
    respuesta_b = pregunta["respuesta_b"]
    respuesta_c = pregunta["respuesta_c"]
        
    respuesta_correcta = pregunta ["respuesta_correcta"]

    txt_pregunta = fuente.render(str(pregunta_elegida), True, color)
    txt_respuesta_a = fuente.render(str(respuesta_a), True, color)
    txt_respuesta_b = fuente.render(str(respuesta_b), True, color)
    txt_respuesta_c = fuente.render(str(respuesta_c), True, color)

    screen.blit(txt_pregunta,(x_pregunta, y_preguntas))
    screen.blit(txt_respuesta_a,(x_izq, y))
    screen.blit(txt_respuesta_b,(x_medio, y))
    screen.blit(txt_respuesta_c,(x_der, y))

    return respuesta_correcta

def verificar_respuesta (evento, lista_posicion, lista_rect)-> bool | None:

    retorno = None

    rect_correcto = lista_rect [0]
    rect_incorrecto1 = lista_rect [1]
    rect_incorrecto2 = lista_rect [2]

    if evento.type == pygame.MOUSEBUTTONDOWN:

        if rect_correcto.collidepoint(lista_posicion):
            retorno = True
        elif rect_incorrecto1.collidepoint(lista_posicion) or rect_incorrecto2.collidepoint(lista_posicion):
            retorno = False

    return retorno