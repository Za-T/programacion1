import pygame
from modulo_aux import *

def preguntar_nombre (screen)->callable:
    fondo = atribuir_fondo ("imagenes\ing_nom.png")
    screen.blit(fondo, (0,0))
    

def mostrar_tablero (screen):
    tablero_png = atribuir_fondo ("imagenes\tablero.png")
    screen.blit(tablero_png, (0,0))