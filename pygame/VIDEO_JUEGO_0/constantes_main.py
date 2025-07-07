import pygame

#MEDIDIAS
ALTO_VENTANA = int(1000)
ANCHO_VENTANA = int(1000)

x_pregunta = 150.2
y_pregunta = 41.3
x_izq = 70
x_medio = 390
x_der = 695
y = 127.5

# Pantallas del juego
pantalla_menu = "menu"
pantalla_jugando = "jugando"
pantalla_score = "puntos"
pantalla_game_over = "game_over"

#COLORES
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HOTPINK = (255, 105, 180)

#RECTANGULOS
rect_mn_puntos = pygame.Rect(377.2, 375, 245.7, 122.8)
rect_mn_jugar = pygame.Rect(359.5, 540.5, 281, 140.5)
rect_mn_salir = pygame.Rect(369, 723.1, 245.7, 122.8)
rect_nom = pygame.Rect(334.7, 265.2, 330.7, 68.5)

rect_preguntas = pygame.Rect(37, 21.8, 905, 78.7)

rect_resultado = pygame.Rect(45, 27.8, 890, 66.7)

rect_a = pygame.Rect(35, 122.5, 300, 50)
rect_b = pygame.Rect(350, 122.5, 300, 50)
rect_c = pygame.Rect(655, 122.5, 300, 50)

rect_tablero_salir = pygame.Rect(942, 1, 59.7, 59.7)

dict_rect = {"a": rect_a, "b": rect_b, "c": rect_c}

#TIMER

SEGUNDOS = 20