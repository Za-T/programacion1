import random 

def mostrar_pregunta (lista_preguntas: list) -> str:

    '''La funcion se encarga de mostrar las preguntas y sus posibles respuestas.
      Una vez que la pregunta fue elegida se elimina.
      Retorna la respuesta correcta.'''

    lista_op= ["a","b","c"]

    pregunta = random.choice(lista_preguntas)

    print(f"\nPregunta: {pregunta["pregunta"]}")

    for op in lista_op:
        print(f"{op}: {pregunta[f"respuesta_{op}"]}")
    
    respuesta_c = pregunta ["respuesta_correcta"]

    lista_preguntas.remove(pregunta)

    return respuesta_c

def verificar_existencia (lista: list) -> bool:

    '''La funcion verifica que la lista no este vacia.'''

    try:
        lista [0]
        retornar = True
    except IndexError:
        retornar = False
    
    return retornar


