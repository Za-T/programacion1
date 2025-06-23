import pygame

def mostrar_tablero ():

    tablero_png = pygame.image.load ("imagenes/tablero.png")
    tablero_png = pygame.transform.scale(tablero_png,(1000,1000))