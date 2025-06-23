import pygame

def atribuir_fondo(ruta: str, size = (1000,1000)):

    pantalla = pygame.image.load (ruta)
    pantalla = pygame.transform.scale(pantalla, size)

    return pantalla
    