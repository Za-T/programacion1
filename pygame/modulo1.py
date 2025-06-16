import random 

def mostrar_pregunta (lista_preguntas: list) -> str:

    lista_op= ["a","b","c"]



    pregunta = random.choice(lista_preguntas)

    print(f"Pregunta: {pregunta["pregunta"]}")

    for op in lista_op:
        print(f"{op}: {pregunta[f"respuesta_{op}"]}")
    
    respuesta_c = pregunta ["respuesta_correcta"]

    lista_preguntas.remove(pregunta)

    return respuesta_c

def verificar_igualdad (valor1, valor2, verdad: str, falso: str) -> bool:
    
    if valor1 == valor2:
        print (f"{verdad}")
        retornar = True
    else:
        print (f"{falso}")
        retornar = False
    
    return retornar

