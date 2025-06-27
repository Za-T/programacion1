import pygame
from copy import deepcopy
from modulo_aux import *

def correr_pantalla_nombre (screen,lista_eventos, color, color_rect, fuente)->callable:

    fondo = atribuir_fondo ("imagenes\ing_nom.png") # \ -> /
    screen.blit(fondo, (0,0))
    pygame.display.flip()
    rect_nombre = pygame.Rect(171.1, 441.6, 657.7, 116.8)

    return pygm_input (screen, lista_eventos, rect_nombre,color_rect, color, fuente)
