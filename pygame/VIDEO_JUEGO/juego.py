import pygame

from constantes_main import *
from menu import *
from run_preguntas import *

from preguntas import *
from score import *

lista_res = leer_csv ("score.csv")
resultado_n = lista_res [0]
#resultado_p = lista_res [0] #corregir

#INICIALIZAR
pygame.init()
screen = pygame.display.set_mode ([ANCHO_VENTANA, ALTO_VENTANA]) #tama;o pantalla
pygame.display.set_caption("Serpientes y escaleras") #titulo

#IMAGENES
tablero_png = pygame.image.load ("imagenes/tablero.png")
tablero_png = pygame.transform.scale(tablero_png,(1000,1000))

menu_png = pygame.image.load ("imagenes/menu_sye.png")
menu_png = pygame.transform.scale(menu_png,(1000,1000))

#Fuente
fuente = pygame.font.SysFont("Arial",30)

#RECTANGULOS
rect_mn_puntos = pygame.Rect(377.2, 275.2, 245.7, 122.8)
rect_mn_jugar = pygame.Rect(359.5, 429.8, 281, 140.5)
rect_mn_salir = pygame.Rect(369, 602.2, 245.7, 122.8)


running = True
primer = True

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
                    pantalla_nombre (screen)
                    primer = False

                if rect_mn_puntos.collidepoint(lista_posicion):
                    mostrar_score(screen, fuente, WHITE)
                    primer = False

                if rect_mn_salir.collidepoint(lista_posicion):
                    running = False

    pygame.display.flip() #actualiza la ventana

pygame.quit()