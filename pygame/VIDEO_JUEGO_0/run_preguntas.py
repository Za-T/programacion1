import pygame
from copy import deepcopy
from modulo_aux import *
from constantes_main import *
from tablero import *
import random

def mostrar_pregunta (screen, pregunta, fuente, color):
    
    pregunta_elegida = pregunta["pregunta"]
    respuesta_a = pregunta["respuesta_a"]
    respuesta_b = pregunta["respuesta_b"]
    respuesta_c = pregunta["respuesta_c"]

    txt_pregunta = fuente.render(str(pregunta_elegida), True, color)
    txt_respuesta_a = fuente.render(str(respuesta_a), True, color)
    txt_respuesta_b = fuente.render(str(respuesta_b), True, color)
    txt_respuesta_c = fuente.render(str(respuesta_c), True, color)

    screen.blit(txt_pregunta,(x_pregunta, y_pregunta))
    screen.blit(txt_respuesta_a,(x_izq, y))
    screen.blit(txt_respuesta_b,(x_medio, y))
    screen.blit(txt_respuesta_c,(x_der, y))
 
def obtener_respuesta_j (evento, lista_posicion:list)->str:

    retorno = None

    if evento.type == pygame.MOUSEBUTTONDOWN:

        if rect_a.collidepoint(lista_posicion):
            retorno = "a"
        elif rect_b.collidepoint(lista_posicion):
            retorno = "b"
        elif rect_c.collidepoint(lista_posicion):
            retorno = "c"
    
    return retorno

def procesar_resultado (respuesta_c, respuesta_j) -> bool:
    
    print (respuesta_j)
    if respuesta_j == respuesta_c:
        resultado_ronda = True
    else:
        resultado_ronda = False
    
    return resultado_ronda
                
def calcular_posicion (respuesta_c, respuesta_j, posicion_j:int, tablero: list, screen, fuente) -> int:
    
    mensaje = None
    txt_siguiente = "SIGUIENTE"

    if posicion_j != 0 and posicion_j != 30:
       
        if respuesta_j == respuesta_c: #respuesta correcta

            posicion_j += 1

            if tablero [posicion_j] != 0:
                mensaje = f"Correcto! Caiste en escalera, adelantas {tablero [posicion_j]} casilleros extra."
                posicion_j += tablero [posicion_j]
            else:
                mensaje = "Correcto! Adelantas 1 casillero."
        else:
            posicion_j -= 1
            if tablero [posicion_j] != 0:            
                mensaje = f"Incorrecto! Caiste en serpiente, regresas {tablero [posicion_j]} casilleros extra."
                posicion_j -= tablero [posicion_j]
            else:
                mensaje = "Incorrecto! Regresas 1 casillero."
        
        if mensaje != None:
            txt_mensaje = fuente.render(str(mensaje), True, BLACK)
            txt_siguiente = fuente.render(txt_siguiente, True, BLACK)
            pygame.draw.rect(screen, WHITE, rect_resultado)
            pygame.draw.rect(screen, WHITE, rect_a)
            pygame.draw.rect(screen, WHITE, rect_b)
            pygame.draw.rect(screen, WHITE, rect_c)

            screen.blit(txt_mensaje,(x_pregunta, y_pregunta))
            screen.blit(txt_siguiente,(x_medio, y))

    return posicion_j

#def dibujar_posicion ():

def manejar_tablero (screen, preguntas_c, tablero, reloj, gestion_tablero:list, fuente, evento, lista_posicion: list):
    
    "La funcion maneja el tablero. Primero elige una pregunta random, una vez que la tiene, empieza un timer, d"
    "Se muestra la pregunta elegida, y las opciones para contestar, "
    "si coliciona con el rectangulo correcto avanza la posicion del tablero, "
    "si es con el incorrecto vuelve para atras"
    "En caso de que el timer (20 seg) se acaba y no hubo una colision, se toma como respuesta incorrecta"

    posicion_j = gestion_tablero [2]

    if evento.type == pygame.MOUSEBUTTONDOWN:
        if rect_tablero_salir.collidepoint(lista_posicion):
            gestion_tablero [0] = False

    existencia = verificar_existencia (preguntas_c)

    if existencia == True and gestion_tablero[0] == True:

        if gestion_tablero [1] == None: #si no hay pregunta, elegirla
            pregunta = random.choice(preguntas_c)
            gestion_tablero [1] = pregunta
            atribuir_fondo ("imagenes/tablero.png",screen)

        else: #hay pregunta elegida
            pregunta = gestion_tablero [1]
            timer_event = pygame.USEREVENT + 1 #configurar timer
            pygame.time.set_timer(timer_event, 1000)

            if gestion_tablero [3] == None: #mostrar la pregunta lo que dure el timer, o hasta que haya una colicion
                mostrar_pregunta (screen, pregunta, fuente, BLACK) 

            respuesta_c = gestion_tablero [1] ["respuesta_correcta"]
            respuesta_j = obtener_respuesta_j(evento, lista_posicion)
            
            if gestion_tablero [3] == None: #si no hay respuesta elegida, guardar None
                gestion_tablero [3] = respuesta_j

            else: #una vez que deja de ser None
                respuesta_j = gestion_tablero [3] #respuesta del jugador

                if gestion_tablero[4] == False:  # Si no se ha mostrado el resultado
                    posicion_j = calcular_posicion(respuesta_c, respuesta_j, posicion_j, tablero, screen, fuente)
                    gestion_tablero[2] = posicion_j
                    gestion_tablero[4] = True  # Marcar que ya se mostró el resultado

                else:#una vez se mostro el resultado
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        if rect_c.collidepoint(lista_posicion):
                            preguntas_c.remove(pregunta)
                            gestion_tablero [1] = None #elegir pregunta nueva

    else:
        gestion_tablero [0] = False #si no hya mas preguntas, terminar juego

    return gestion_tablero      
