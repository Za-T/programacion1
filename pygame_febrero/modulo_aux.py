import pygame

def verificar_existencia (lista: list) -> bool:

    '''La funcion verifica que la lista no este vacia.

    Parametro:
        lista: la lista que se busca comprobar.

    Retorno:
        True si existe
        False si no.'''

    try:
        lista [0]
        retornar = True
    except IndexError:
        retornar = False
    
    return retornar

def atribuir_fondo(ruta: str, screen, size = (1000,1000)):

    pantalla = pygame.image.load (ruta)
    pantalla = pygame.transform.scale(pantalla, size)
    screen.blit(pantalla, (0,0))
