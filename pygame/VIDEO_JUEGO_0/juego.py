import pygame

from constantes_main import *
from menu import *
from run_preguntas import *
from pantalla_nombre import *
from tablero import *

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

def jugar_sye():

    #Incializar
    pygame.init()
    screen = pygame.display.set_mode([ANCHO_VENTANA, ALTO_VENTANA])  # tamaño pantalla
    pygame.display.set_caption("Serpientes y escaleras")  # titulo
    reloj = pygame.time.Clock()

    #FUENTES
    FUENTE = pygame.font.SysFont("Arial", 30)

    #Pantalla
    pantalla_actual = pantalla_menu
    running = True
    
    #Nombre y estado del input
    txt_nombre = ""
    input_activo = False
    
    #Posicion Mouse
    lista_posicion = []
    
    #Tablero
    #0.correr tablero, 1.pregunta elegida, 2.posicion jugador,
    gestion_tablero = [True, None, 15, None]
    correr_tablero = gestion_tablero [0]
    resultado_ronda = None

    while running == True:

        lista_eventos = pygame.event.get()
        
        # Procesar cada evento
        for evento in lista_eventos:

            if evento.type == pygame.QUIT:
                running = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_posicion = list(evento.pos)
            
            match pantalla_actual:

                case False:
                    running = False
                    
                case "menu": 
                    lista_menu = generar_menu(evento, lista_posicion, screen, FUENTE, txt_nombre, input_activo)
                    txt_nombre = lista_menu[0]
                    input_activo = lista_menu[2]
                    if lista_menu[1] != None:  # Si hay cambio de pantalla
                        pantalla_actual = lista_menu[1]
                        
                case "jugando":
                    if correr_tablero == True:
                        gestionar_tablero = manejar_tablero(screen, preguntas_c, tablero, reloj, gestion_tablero, FUENTE, evento, lista_posicion)
                        correr_tablero = gestionar_tablero[0]
                        posicion_jugador = gestion_tablero [2]
                    else:
                        pantalla_actual = "game_over"
                        
                case "puntos":
                    mostrar_score(screen, FUENTE, WHITE)
                    
                case "game_over":
                    running = False

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

jugar_sye()