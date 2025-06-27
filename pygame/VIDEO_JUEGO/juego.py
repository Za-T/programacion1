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

#FONDOS
tablero_png = pygame.image.load ("imagenes/tablero.png")
tablero_png = pygame.transform.scale(tablero_png,(1000,1000))

menu_png = pygame.image.load ("imagenes/menu_sye.png")
menu_png = pygame.transform.scale(menu_png,(1000,1000))

#RECTANGULOS
rect_mn_puntos = pygame.Rect(377.2, 275.2, 245.7, 122.8)
rect_mn_jugar = pygame.Rect(359.5, 429.8, 281, 140.5)
rect_mn_salir = pygame.Rect(369, 602.2, 245.7, 122.8)

rect_a = pygame.Rect(35, 122.5, 300, 50)
rect_b = pygame.Rect(350, 122.5, 300, 50)
rect_c = pygame.Rect(655, 122.5, 300, 50)

#Fuente
FUENTE = pygame.font.SysFont("Arial", 30) #pq si pongo fuente en otro archivo no lo toma?

running = True
primer = True
nombre = None
respuesta_correcta = None

while running == True:

    lista_eventos = pygame.event.get ()
    
    #menu inicio
    if primer == True:
        screen.blit(menu_png, (0,0))

    for evento in lista_eventos:

        if evento.type == pygame.QUIT:
            running = False

        if primer == True:
            screen.blit(menu_png, (0,0))

            if evento.type == pygame.MOUSEBUTTONDOWN:
                lista_posicion = list (evento.pos)

                #Decidir que hacer en el menu
                if rect_mn_jugar.collidepoint(lista_posicion):
                    nombre = correr_pantalla_nombre (screen, lista_eventos, WHITE, BLACK, FUENTE)
                    primer = False

                if rect_mn_puntos.collidepoint(lista_posicion):
                    mostrar_score(screen, FUENTE, WHITE)
                    primer = False

                if rect_mn_salir.collidepoint(lista_posicion):
                    running = False
        
        if nombre != None:

            existencia = verificar_existencia (preguntas_c)

            if existencia == True:

                respuesta_correcta = mostrar_preguntas (screen, FUENTE, BLACK, preguntas_c)

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
                print ("terminar juego")

    pygame.display.flip() #actualiza la ventana

pygame.quit()