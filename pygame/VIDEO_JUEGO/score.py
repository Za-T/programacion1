from csv import *
from copy import deepcopy
from imagenes import *
from modulo_aux import *

def leer_archivo (nombre:str)-> list:
    
    try:
        with open(nombre, 'r') as archivo:
            lista_lineas = archivo.readlines()
    
    except FileNotFoundError:
        print ("Ese archivo no existe.")
        lista_lineas =[]

    return lista_lineas

def mostrar_score (screen, fuente, color):

    score_png = atribuir_fondo ("imagenes/Score.png")
    screen.blit(score_png, (0,0))

    lista_res = leer_archivo ("score.csv")

    x_izq = 120
    x_der = 574.6
    y_izq = 181.3
    y_der = deepcopy(y_izq)
    diferencia = 129
      
    for i in range(10): #asume que hay 10, arreglar
        
        resultado_n = lista_res [i]
        #resultado_p = lista_res [i] #corregir

        txt_resultado_n = fuente.render(str(resultado_n), True, color)
                    
        #txt_resultado_p = fuente.render(str(resultado_p), True, BLACK)

        if i % 2 == 0:
            y_izq += diferencia  
            posc_imp = [x_izq,y_izq] 
               
        else:
            y_der += diferencia
            posc_imp = [x_der,y_der]
            
        screen.blit(txt_resultado_n,posc_imp)