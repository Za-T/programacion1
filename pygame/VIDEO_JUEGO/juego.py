import pygame

from constantes_main import *
from menu import *
from run_preguntas import *
from pantalla_nombre import *

from preguntas import *
from score import *

'''Falta:

    Modularizar el menu
    Anadir sonido 
    Mostrar preguntas
    Acceder al menu en todo momento
    Cronometro
    Ordenar lista de puntaje

'''

#INICIALIZAR
pygame.init()
screen = pygame.display.set_mode ([ANCHO_VENTANA, ALTO_VENTANA]) #tama;o pantalla
pygame.display.set_caption("Serpientes y escaleras") #titulo
clock = pygame.time.Clock()

#Fuente
FUENTE = pygame.font.SysFont("Arial", 30)

#Variables de estado
estado_actual = ESTADO_MENU
running = True
nombre = None
respuesta_correcta = None
posicion_jugador = 15

while running == True:

    lista_eventos = pygame.event.get ()
    
    for evento in lista_eventos:

        if evento.type == pygame.QUIT:
            running = False

        elif evento.type == pygame.MOUSEBUTTONDOWN:
                lista_posicion = list (evento.pos)

                match estado_actual:

                    case False:
                        running = False

                    case "menu": 
                        estado_actual = generar_menu(evento, lista_posicion, screen, estado_actual)

                    case "nombre":

                        nombre = correr_pantalla_nombre(screen, lista_eventos, WHITE, BLACK, FUENTE)
            
                        if nombre != None: 
                            nombre = nombre
                            estado_actual = ESTADO_JUGANDO

                    case "jugando":
                        existencia = verificar_existencia (preguntas_c)

                        if existencia:
                            respuesta_correcta = mostrar_preguntas(screen, FUENTE, BLACK, preguntas_c)
                            esperando_respuesta = True

                            match respuesta_correcta:
                                case "a":
                                    rect_correcto = rect_a
                                    rect_incorrecto1 = rect_b
                                    rect_incorrecto2 = rect_c
                                case "b":
                                    rect_correcto = rect_b
                                    rect_incorrecto1 = rect_a
                                    rect_incorrecto2 = rect_c
                                case "c":
                                    rect_correcto = rect_c
                                    rect_incorrecto1 = rect_a
                                    rect_incorrecto2 = rect_b

                            if respuesta_correcta != None:
                                resultado_ronda = verificar_respuesta (evento, lista_posicion, rect_correcto, rect_incorrecto1, rect_incorrecto2)
                    
                        if resultado_ronda != None:
                            print (resultado_ronda)

                        else:
                            estado_actual = ESTADO_GAME_OVER

                    case "puntos":
                        mostrar_score (screen, FUENTE, WHITE)

                    case "game_over":
                        print ("f")
                        running = False
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()