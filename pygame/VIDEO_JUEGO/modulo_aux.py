import pygame

def pygm_input (screen:vars, lista_eventos, rectangulo:vars, color_rect:tuple, color: tuple, fuente:vars)-> str:

    txt = ""
    activo = False
    
    for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:   
                activo = rectangulo.collidepoint(evento.pos)

            if evento.type == pygame.KEYDOWN:
                if activo != False:            
                    if evento.key == pygame.K_RETURN:
                        return txt
                    elif evento.key == pygame.K_BACKSPACE:
                        txt = txt[:-1]
                    else:
                        txt += evento.unicode

    pygame.draw.rect(screen, color_rect, rectangulo)
    font_input_surface = fuente.render(txt, True, color) 
    screen.blit(font_input_surface, ( rectangulo.x + 15, rectangulo.y + 15 ))
      

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
    