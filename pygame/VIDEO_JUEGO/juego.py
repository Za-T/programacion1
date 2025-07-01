import pygame

from constantes_main import *
from menu import *
from run_preguntas import *
from pantalla_nombre import *

from preguntas import *
from score import *

'''Falta:
    Anadir sonido 
    Acceder al menu en todo momento
    movimiento
    Cronometro
    fin del juego
    ciudadanos primera clases
    Ordenar lista de puntaje
'''

def jugar_sye ():

    #Incializar
    pygame.init()
    screen = pygame.display.set_mode ([ANCHO_VENTANA, ALTO_VENTANA]) #tama;o pantalla
    pygame.display.set_caption("Serpientes y escaleras") #titulo
    clock = pygame.time.Clock()
    #Fuente
    FUENTE = pygame.font.SysFont("Arial", 30)
    #Pantalla
    pantalla_actual = pantalla_menu
    running = True
    #Nombre
    txt_nombre = ""
    #Posicion Mouse
    lista_posicion = []
    #Tablero
    correr_tablero = True
    gestion_preguntas = [True, None, None, None]
    resultado_ronda = None
    posicion_jugador = 15

    while running == True:

        lista_eventos = pygame.event.get ()
        for evento in lista_eventos:

            if evento.type == pygame.QUIT:
                running = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                    lista_posicion = list (evento.pos)
            
            match pantalla_actual:

                case False:
                            running = False
                case "menu": 
                            pantalla_actual = generar_menu(evento, lista_posicion, screen, pantalla_actual)
                case "nombre":
                    lista_nombre = correr_pantalla_nombre(screen, evento, WHITE, BLACK, FUENTE, txt_nombre)
                    txt_nombre = lista_nombre [0]
                    nombre_final = lista_nombre [1]
                    if nombre_final != "":
                        pantalla_actual = pantalla_jugando
                case "jugando":
                        if correr_tablero == True:
                                lista_tablero = manejar_tablero(preguntas_c, dict_rect, screen, evento, lista_posicion, gestion_preguntas, FUENTE, BLACK)
                                correr_tablero = lista_tablero [0]
                case "puntos":
                            mostrar_score (screen, FUENTE, WHITE)
                case "game_over":
                            running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

jugar_sye ()