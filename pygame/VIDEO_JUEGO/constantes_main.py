import pygame

#MEDIDIAS
ALTO_VENTANA = int(1000)
ANCHO_VENTANA = int(1000)

# Estados del juego
ESTADO_MENU = "menu"
ESTADO_NOMBRE = "nombre"
ESTADO_JUGANDO = "jugando"
ESTADO_PUNTOS = "puntos"
ESTADO_GAME_OVER = "game_over"

#COLORES
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HOTPINK = (255, 105, 180)

#RECTANGULOS
rect_mn_puntos = pygame.Rect(377.2, 275.2, 245.7, 122.8)
rect_mn_jugar = pygame.Rect(359.5, 429.8, 281, 140.5)
rect_mn_salir = pygame.Rect(369, 602.2, 245.7, 122.8)

rect_a = pygame.Rect(35, 122.5, 300, 50)
rect_b = pygame.Rect(350, 122.5, 300, 50)
rect_c = pygame.Rect(655, 122.5, 300, 50)

