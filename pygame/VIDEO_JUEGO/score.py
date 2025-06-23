from csv import *
import pygame
from imagenes import *
from modulo_aux import *

def leer_csv (nombre:str)-> list:
    
    try:
        with open(nombre, 'r') as archivo:
            lista_lineas = archivo.readlines()

        return lista_lineas
    
    except FileNotFoundError:
        print ("Ese archivo no existe.")

def mostrar_score (screen, fuente, color):

    score_png = atribuir_fondo ("imagenes/Score.png")

    screen.blit(score_png, (0,0))

    lista_res = leer_csv ("score.csv")

    posc_imp = [110,181.3]  

    for i in range(10): #asume que hay 10, arreglar

        resultado_n = lista_res [i]
        #resultado_p = lista_res [i] #corregir

        txt_resultado_n = fuente.render(str(resultado_n), True, color)
                    
        #txt_resultado_p = fuente.render(str(resultado_p), True, BLACK)

        posc_imp [1] += 129.3
                   

        screen.blit(txt_resultado_n,posc_imp)