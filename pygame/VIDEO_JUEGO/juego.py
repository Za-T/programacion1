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

#INICIALIZAR
pygame.init()
screen = pygame.display.set_mode ([ANCHO_VENTANA, ALTO_VENTANA]) #tama;o pantalla
pygame.display.set_caption("Serpientes y escaleras") #titulo
clock = pygame.time.Clock()

#Fuente
FUENTE = pygame.font.SysFont("Arial", 30)

#Variables de estado
pantalla_actual = pantalla_menu
running = True
txt_nombre = ""
respuesta_correcta = None
posicion_jugador = 15
resultado_ronda = None
lista_posicion = []

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
                        existencia = verificar_existencia (preguntas_c)
                        if existencia == True:
                            respuesta_correcta = mostrar_preguntas(screen, FUENTE, BLACK, preguntas_c)
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
                            pantalla_actual = pantalla_game_over
            case "puntos":
                        mostrar_score (screen, FUENTE, WHITE)
            case "game_over":
                        print ("f")
                        running = False
                
        


    pygame.display.flip()
    clock.tick(60)


pygame.quit()