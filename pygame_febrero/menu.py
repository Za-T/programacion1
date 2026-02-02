import pygame
from modulo_aux import *
from constantes_main import *

def pygm_input(screen, evento, rectangulo, color_rect, color_fuente, fuente, txt_actual):
    """
    Función para manejar input de texto
    txt_actual: el texto actual que se va acumulando
    """
    txt_nombre = txt_actual  # Mantener el texto actual
    
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_BACKSPACE:
            txt_nombre = txt_nombre[:-1]  # Eliminar último carácter
        else:
            # Solo agregar caracteres imprimibles
            if evento.unicode.isprintable():
                txt_nombre += evento.unicode

    # Dibujar el rectángulo y el texto
    pygame.draw.rect(screen, color_rect, rectangulo)
    font_input_surface = fuente.render(txt_nombre, True, color_fuente) 
    screen.blit(font_input_surface, (rectangulo.x + 15, rectangulo.y + 15))
    
    return txt_nombre

def generar_menu(evento, lista_posicion, screen, FUENTE_NOMBRE, txt_nombre_actual="", input_activo=False):
    """
    Función para generar el menú
    txt_nombre_actual: el nombre actual del jugador
    input_activo: si el campo de input está activo
    """
    
    atribuir_fondo("imagenes/menu_sye.png", screen)

    lista_menu = [txt_nombre_actual, None, input_activo]  # 0. Nombre, 1. pantalla, 2. input_activo

    # Procesar eventos
    if evento.type == pygame.MOUSEBUTTONDOWN:

        if rect_nom.collidepoint(lista_posicion):
            # Activar input de texto
            lista_menu[2] = True  # input_activo = True
        else:
            # Si se hace click fuera del campo de nombre, desactivar input
            lista_menu[2] = False

    # Si el input está activo, procesar el texto
    if input_activo == True:
        if evento.type == pygame.KEYDOWN:
            lista_menu[0] = pygm_input(screen, evento, rect_nom, BLACK, WHITE, FUENTE_NOMBRE, txt_nombre_actual)

    pygame.draw.rect(screen, BLACK, rect_nom)
    font_input_surface = FUENTE_NOMBRE.render(txt_nombre_actual, True, WHITE) 
    screen.blit(font_input_surface, (rect_nom.x + 15, rect_nom.y + 15))
    
    if lista_menu [0] != None and lista_menu [0] != "":
            if rect_mn_jugar.collidepoint(lista_posicion):
                lista_menu[1] = pantalla_jugando
            elif rect_mn_puntos.collidepoint(lista_posicion):
                lista_menu[1] = pantalla_score
            elif rect_mn_salir.collidepoint(lista_posicion):
                lista_menu[1] = False

    return lista_menu
    
