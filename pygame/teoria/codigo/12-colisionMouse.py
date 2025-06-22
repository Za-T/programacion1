import pygame
#iniciar la pantalla
pygame.init()
#COLORES
ANCHO_VENTANA = 500
ALTO_VENTANA = 500
COLOR_CELESTE = ( 0, 0,128)
RED1 = (255, 0, 0)
posicion_rana = [100, 100]
flag_mostrar = True

#IMAGENES
imagen_rana = pygame.image.load("ranasentada.jpg")
imagen_rana = pygame.transform.scale(imagen_rana,(100,100)) #puedo cambiar el tamaño de la imagen

#defino el área/superficie/rectángulo de mi imagen left, top, ancho, alto
rect_rana = imagen_rana.get_rect()
#puedo indicarle en que coordenadas lo quiero y con que tamaño
rect_rana.x = 140
rect_rana.y = 125
rect_rana.width = 20
rect_rana.height = 20

#crear la pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
#Seteo un título en la pantalla
pygame.display.set_caption("Juego")
flag_correr = True
while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rect_rana.collidepoint(evento.pos):
                flag_mostrar = False

    #fondo color
    pantalla.fill(COLOR_CELESTE)
    if flag_mostrar:
        pantalla.blit(imagen_rana,posicion_rana)  #fundir la imagen en una superficie
        pygame.draw.rect(pantalla, RED1,rect_rana) 

    #mostrar
    pygame.display.flip()
pygame.quit()
