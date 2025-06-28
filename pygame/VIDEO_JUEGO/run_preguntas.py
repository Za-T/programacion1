import pygame
from copy import deepcopy
from modulo_aux import *
import random

def mostrar_preguntas (screen, fuente, color, lista_preguntas) -> str:

    atribuir_fondo ("imagenes/tablero.png",screen)

    x_pregunta = 35.2
    y_preguntas = 21.3

    x_izq = 35
    x_der = 574.6
    x_medio = 350
    y = 181.3
   
    pregunta = random.choice(lista_preguntas)
    lista_preguntas.remove(pregunta)
    
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

def verificar_respuesta (evento, lista_posicion, rect_correcto, rect_incorrecto1, rect_incorrecto2)-> bool | None:

    if evento.type == pygame.MOUSEBUTTONDOWN:

        if rect_correcto.collidepoint(lista_posicion):
            retorno = True

        elif rect_incorrecto1.collidepoint(lista_posicion) or rect_incorrecto2.collidepoint(lista_posicion):
            retorno = False
        
        else:
            retorno = None

    return retorno