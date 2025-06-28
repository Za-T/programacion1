import pygame
from modulo_aux import *
from constantes_main import *

def generar_menu (evento, lista_posicion, screen, estado_actual):

    atribuir_fondo ("imagenes/menu_sye.png", screen)

    if evento.type == pygame.MOUSEBUTTONDOWN:
            if rect_mn_jugar.collidepoint(lista_posicion):
                estado_actual = ESTADO_NOMBRE
            elif rect_mn_puntos.collidepoint(lista_posicion):
                estado_actual = ESTADO_PUNTOS
            elif rect_mn_salir.collidepoint(lista_posicion):
                estado_actual = False

    return estado_actual 
    
