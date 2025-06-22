import pygame

from constantes_main import *
from preguntas import *
from score import *

lista_res = leer_csv ("score.csv")
resultado_n = lista_res [0] ["Nombre"]
resultado_p = lista_res [0] ["Puntos"]


#INICIALIZAR
pygame.init()
screen = pygame.display.set_mode ([ANCHO_VENTANA, ALTO_VENTANA]) #tama;o pantalla
pygame.display.set_caption("Serpientes y escaleras") #titulo

#IMAGENES
tablero_png = pygame.image.load ("imagenes/tablero.png")
tablero_png = pygame.transform.scale(tablero_png,(1000,1000))

menu_png = pygame.image.load ("imagenes/menu.png")
menu_png = pygame.transform.scale(menu_png,(1000,1000))

#Definir texto
fuente = pygame.font.render("Arial",30)
txt_resultado_n = fuente.render(str(resultado_n), True, BLACK)
txt_resultado_p = fuente.render(str(resultado_p), True, BLACK)




#RECTANGULOS
rect_mn_jugar = pygame.Rect(350,500,300,78.2)
rect_mn_score = pygame.Rect(350,610.2,300,78.2)
rect_mn_salir = pygame.Rect(350,720.3,300,78.2)


running = True
primer = True

while running == True:

    #menu inicio
    if primer == True:
        screen.blit(menu_png, (0,0))
        primer = False

    lista_eventos = pygame.event.get ()

    for evento in lista_eventos:

        if evento.type == pygame.QUIT:
            running = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            lista_posicion = list (evento.pos)

            #Decidir que hacer en el menu
            if rect_mn_jugar.collidepoint(lista_posicion):
                screen.blit(tablero_png, (0,0))
            if rect_mn_score.collidepoint(lista_posicion):
                print("score")
            if rect_mn_salir.collidepoint(lista_posicion):
                running = False

    pygame.display.flip() #actualiza la ventana

pygame.quit()