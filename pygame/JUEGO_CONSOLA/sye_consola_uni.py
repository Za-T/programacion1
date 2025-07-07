tablero = [0, 1, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 2, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0]

#fun_preguntas
import random 

def mostrar_pregunta (lista_preguntas: list) -> str:

    '''
      La funcion se encarga de mostrar las preguntas y sus posibles respuestas.
      Una vez que la pregunta fue elegida se elimina.

      Parametros:
        lista_preguntas: lista de diccionarios con las preguntas y respuestas.

      Retorno:
        Un string con la respuesta correcta.'''

    lista_op= ["a","b","c"]

    pregunta = random.choice(lista_preguntas)

    print(f"\nPregunta: {pregunta["pregunta"]}")

    for op in lista_op:
        print(f"{op}: {pregunta[f"respuesta_{op}"]}")
    
    respuesta_c = pregunta ["respuesta_correcta"]

    lista_preguntas.remove(pregunta)

    return respuesta_c

#fun_posicion
def actualizar_posicion_mov (tablero:list, posicion: int, resultado_res:bool) -> int:
    
    '''La funcion se encargar de verificar cual es la nueva posicion a la que se tiene que mover el jugador.
        Ademas le informa si cayo en escalera o serpiente, y cuantos casilleros debe saltearse.
        
        Parametros:
            tablero: lista que representa el orden del tablero.
            posicion: posición actual del jugador.
            resultado_res: valor booleano que indica si fue correcta la respuesta del jugador.
        
        Retorno:
          Un entero con la nueva posicion.'''

    if posicion != 0 and posicion != 30:
       
        if resultado_res == True:

            posicion += 1

            if tablero [posicion] != 0:
                print (f"Caiste en escalera, adelantas {tablero [posicion]} casilleros.\n")
                posicion += tablero [posicion]

        else:

            posicion -= 1

            if tablero [posicion] != 0:            
                print (f"Caiste en serpiente, regresas {tablero [posicion]} casilleros.\n")
                posicion -= tablero [posicion]

    return posicion

#fun_final.py
def escribir_archivo (ruta:str, dato1:str, dato2: int):

    '''La funcion escribe los parametros, dato1 y dato2, dentro del archivo csv
        
        Parametros:
            ruta: ubicación del archivo.
            dato1: primer dato a guardar.
            dato2: segundo dato a guardar.
        '''

    with open(ruta, "a") as archivo:
        archivo.write(f"{dato1},{dato2}\n")

def finalizar_juego (nombre:str, posicion:int,):

    '''La funcion se encarga de informar que el juego finalizo, a que posicion llego, 
    y ejecuta la funcion encargada de escribir los resultados en csv
    
    Parametros:
        nombre: cadena con el nombre del jugador
        posicion: posición final en el tablero.'''

    print (f"\n{nombre} llego a la posicion {posicion}.")
    print (f"Fin del juego.")
    escribir_archivo("Score.csv", posicion, nombre)

#fun_aux

def solicitar_str (nombre_valor: str) -> str:

    '''Solicita al usuario el ingreso de una cadena y la retorna.
        Parametro:
            nombre_valor: el nombre del valor a ingresar'''
    
    cadena = str (input (f"Ingresar {nombre_valor}: "))
    return cadena

def validar_str (texto: str, op1: str, op2: str, op3: str = None) -> str:

    '''Validar que la cadena de caracteres ingresada este disponible entre 2 o 3 opciones.

    Parametros:
        texto: Texto que se muestra para indicarle al usuario que debe ingresar un valor. 
        op1: Opcion 1 a elegir
        op2: Opcion 2 a elegir,
        op3: Opcion 3 a elegir. Se asume que esta opcion esta vacia, 
        si en los parametros reales se ingresa un valor, entonces ahi se muestra esta opcion.

    Retorno:
        Retorna la respuesta elegida dentro de las opciones validas.'''

    if op3 != None:
        cadena = input (f"{texto} ({op1},{op2},{op3}): ")
        while cadena != op1 and cadena != op2 and cadena != op3:
            cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2},{op3}): "))

    else:
        cadena = input (f"{texto} ({op1},{op2}): ")
        while cadena != op1 and cadena != op2:
            cadena = (input (f"Error, valor ingresado no valido. Ingrese un nuevo valor ({op1},{op2}): "))
    
    return cadena

def continuar_juego (pregunta:str) -> bool:

    '''Verifica si el usuario quiere continuar el juego.

    Parametros
        pregunta =  texto de la pregunta a mostrar al usuario.

    Retorno: un booleano, 
        True si quiere continuar. 
        False si no quiere continuar.'''

    respuesta = validar_str (pregunta,"s","n")

    if respuesta == "s":
        respuesta = True
    else:
        respuesta = False

    return respuesta

def verificar_igualdad (valor1, valor2, verdad: str, falso: str) -> bool:

    '''Verifica si los parametros, valor1 y valor2, son iguales.

    Parametros:
        valor1: primer valor a comparar.
        valor2: segundo valor a comparar.
        verdad: mensaje a mostrar si es verdadero.
        falso: mensaje a mostar si es falso.

    Retorno:
        True si es igual.
        False si no es igual.'''
    
    if valor1 == valor2:
        print (f"\n{verdad}")
        retornar = True
    else:
        print (f"\n{falso}")
        retornar = False
    
    return retornar

def verificar_existencia (lista: list) -> bool:

    '''La funcion verifica que la lista no este vacia.

    Parametro:
        lista: la lista que se busca comprobar.

    Retorno:
        True si existe
        False si no.'''

    try:
        lista [0]
        retornar = True
    except IndexError:
        retornar = False
    
    return retornar

#consola

from preguntas import *

def jugar_sye (tablero:list, lista_preguntas:list):

    ''' 
        La fucion jugar_sye se encarga de ejecutar todas las funciones necesesarias para correr el juego.

        Parametros:
            tablero: lista que representa el orden del tablero.
            lista_preguntas: lista de diccionarios que contiene las preguntas y respuestas del juego.
        
    '''
    
    nombre = solicitar_str ("nombre del jugador")

    jugar = continuar_juego (f"¿{nombre}, vas a jugar?")

    posicion = 15

    while jugar == True:

        preguntas = verificar_existencia (lista_preguntas)

        if preguntas == True:

            respuesta_c = mostrar_pregunta (lista_preguntas)

            respuesta_j = validar_str ("\nIngrese su respuesta","a","b","c")

            resultado_res = verificar_igualdad (respuesta_c, respuesta_j, "Correcto!\n", "Incorrecto!\n")
                
            posicion = actualizar_posicion_mov (tablero, posicion, resultado_res)
            
            match posicion:

                case 0:
                    print ("Perdiste.")
                    jugar = False
                
                case 30:
                    print ("Ganaste.")
                    jugar = False
                
                case _:
                    print (f"Tu posicion actual es {posicion}\n")
                    jugar = continuar_juego (f"¿Continuar jugando?")
               
        else:
            print ("\nNo hay mas preguntas.")
            jugar = False
        
    finalizar_juego (nombre, posicion)
        
jugar_sye (tablero, preguntas_c)