import pygame
from copy import deepcopy
from modulo_aux import *
 
def pygm_input (screen, evento, rectangulo, color_rect, color, fuente, txt_actual):

    txt_final = ""

    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RETURN and len(txt_actual) > 0:
            txt_final = txt_actual
        elif evento.key == pygame.K_BACKSPACE:
            txt_actual = txt_actual[:-1]
        else:
            if evento.unicode and evento.unicode.isprintable():
                txt_actual += evento.unicode

    retorno = [txt_actual, txt_final]

    pygame.draw.rect(screen, color_rect, rectangulo)
    font_input_surface = fuente.render(txt_actual, True, color) 
    screen.blit(font_input_surface, (rectangulo.x + 15, rectangulo.y + 15))
    
    return retorno

def correr_pantalla_nombre(screen, lista_eventos, color, color_rect, fuente, txt_nombre):
    """
    Función principal para manejar la pantalla de nombre
    Retorna: (texto_actualizado, nombre_completo_o_None)
    """
    atribuir_fondo("imagenes/ing_nom.png", screen)
    
    rect_nombre = pygame.Rect(161.7, 431.6, 687.6, 140.2)
    
    return pygm_input(screen, lista_eventos, rect_nombre, color_rect, color, fuente, txt_nombre)
    
    