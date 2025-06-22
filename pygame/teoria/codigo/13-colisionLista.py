'''
La función collidelist verifica si el rectángulo del jugador colisiona con alguno de los rectángulos en la lista obstaculos. 
    Si hay colisión, devuelve el índice del primer rectángulo con el que colisionó. 
    Si no hay colisión, devuelve -1.

Movimiento: El jugador se mueve con las teclas de dirección (flechas).

Detección de colisión: Si el jugador colide con algún obstáculo, su color cambia a verde.
'''


import pygame

# Inicializamos Pygame
pygame.init()

# Dimensiones de la ventana
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Ejemplo de Collidelist')

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Creamos los rectángulos (x, y, ancho, alto)
jugador = pygame.Rect(100, 100, 50, 50)
obstaculos = [
    pygame.Rect(300, 100, 50, 50),
    pygame.Rect(500, 200, 50, 50),
    pygame.Rect(700, 400, 50, 50)
]

# Reloj para controlar la velocidad del juego
reloj = pygame.time.Clock()

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Movimiento del jugador (solo con las teclas de dirección)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= 5
    if teclas[pygame.K_RIGHT]:
        jugador.x += 5
    if teclas[pygame.K_UP]:
        jugador.y -= 5
    if teclas[pygame.K_DOWN]:
        jugador.y += 5

    # Usamos collidelist para detectar colisión con cualquier obstáculo
    obstaculo_colisionado = jugador.collidelist(obstaculos)

    # Pintamos el fondo
    pantalla.fill(BLANCO)

    # Dibujamos al jugador y los obstáculos
    pygame.draw.rect(pantalla, AZUL, jugador)
    for obstaculo in obstaculos:
        pygame.draw.rect(pantalla, ROJO, obstaculo)

    # Si hay colisión, cambiamos el color del jugador a verde
    if obstaculo_colisionado != -1:
        pygame.draw.rect(pantalla, VERDE, jugador)

    # Actualizamos la pantalla
    pygame.display.flip()

    # Controlamos los FPS
    reloj.tick(60)

# Cerramos Pygame
pygame.quit()

'''
En Pygame, el método tick() de un objeto Clock es una herramienta que te permite controlar la velocidad 
de actualización de tu juego. 
Se utiliza para establecer un límite en la cantidad de fotogramas por segundo (FPS, por sus siglas en inglés)
a los que debe ejecutarse el bucle principal del juego, lo que garantiza que el juego corra a una velocidad
constante y no dependa de la potencia del hardware o de otros factores externos.

El método tick() toma un parámetro opcional, que es el número de fotogramas por segundo (FPS) al que deseas 
que se ejecute el bucle principal del juego. 
Esto ayuda a mantener un juego más estable y evitar que corra demasiado rápido o demasiado lento. 
Si no se especifica un valor, el reloj se ajusta automáticamente, pero es recomendable fijar un valor para 
tener control sobre la velocidad de ejecución.

'''