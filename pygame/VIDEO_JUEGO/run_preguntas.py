import pygame
from copy import deepcopy
from modulo_aux import *

def pygm_input (rectangulo:vars, color: tuple, fuente:vars)-> str:

    running = True

    while running == True:

        lista_eventos = pygame.event.get ()

        for evento in lista_eventos:

            if evento.type == pygame.QUIT:
                running = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                    
                    lista_posicion = list (evento.pos)

                    if rectangulo.collidepoint(lista_posicion):
                        
                        if evento.type == pygame.KEYDOWN:
                            
                            if evento.key == pygame.K_RETURN:
                                running = False
                            elif evento.key == pygame.K_BACKSPACE:
                                txt = txt[:-1]
                            else:
                                
                        


def pantalla_nombre (screen)->callable:

    fondo = atribuir_fondo ("imagenes\ing_nom.png") # \ -> /
    screen.blit(fondo, (0,0))
    pygame.display.flip()
    rect_nombre = pygame.Rect(left, top, width, height)

    return pygm_input (rect_nombre)

    

def mostrar_tablero (screen):
    tablero_png = atribuir_fondo ("imagenes\tablero.png")
    screen.blit(tablero_png, (0,0))