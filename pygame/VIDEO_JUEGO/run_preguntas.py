import pygame
from copy import deepcopy
from modulo_aux import *

def pygm_input (screen:vars, rectangulo:vars, color_rect:tuple, color: tuple, fuente:vars)-> str:

    running = True

    txt = ""

    activo = False
    
    while running == True:

        pygame.draw.rect(screen, color_rect, rectangulo)

        lista_eventos = pygame.event.get ()

        for evento in lista_eventos:#como hacer sin doble bucle?

            if evento.type == pygame.QUIT:
                running = False

            if evento.type == pygame.MOUSEBUTTONDOWN:   
                activo = rectangulo.collidepoint(evento.pos)

            if evento.type == pygame.KEYDOWN:

                if activo != False:            
                    if evento.key == pygame.K_RETURN:
                        running = False
                    elif evento.key == pygame.K_BACKSPACE:
                        txt = txt[:-1]
                    else:
                        txt += evento.unicode

        font_input_surface = fuente.render(txt, True, color) 
        screen.blit(font_input_surface, ( rectangulo.x + 15, rectangulo.y + 15 ))
        
        #mostrar los cambios en la pantalla
        pygame.display.flip()

    return txt
                                
def pantalla_nombre (screen, color, color_rect, fuente)->callable:

    fondo = atribuir_fondo ("imagenes\ing_nom.png") # \ -> /
    screen.blit(fondo, (0,0))
    pygame.display.flip()
    rect_nombre = pygame.Rect(171.1, 441.6, 657.7, 116.8)

    return pygm_input (screen, rect_nombre,color_rect, color, fuente)

def mostrar_tablero (screen):
    tablero_png = atribuir_fondo ("imagenes\tablero.png")
    screen.blit(tablero_png, (0,0))