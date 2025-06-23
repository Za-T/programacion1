from csv import *
from copy import deepcopy
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

    x_izq = 120
    x_der = 574.6
    y_izq = 181.3
    y_der = deepcopy(y_izq)
      
    for i in range(10): #asume que hay 10, arreglar
        
        resultado_n = lista_res [i]
        #resultado_p = lista_res [i] #corregir

        txt_resultado_n = fuente.render(str(resultado_n), True, color)
                    
        #txt_resultado_p = fuente.render(str(resultado_p), True, BLACK)

        if i % 2 == 0:
            y_izq += 129  
            posc_imp = [x_izq,y_izq] 
               
        else:
            y_der += 129
            posc_imp = [x_der,y_der]
            
        
        
        
        screen.blit(txt_resultado_n,posc_imp)