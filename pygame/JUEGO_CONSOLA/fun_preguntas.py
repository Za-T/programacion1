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




