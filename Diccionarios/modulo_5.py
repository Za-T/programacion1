from estudiantes import *
from biblioteca_funciones import *

def asignar_valores_prom (valor) -> dict:
    
    datos_prom = {
        "promedio_mayor" : valor ["promedio"],
        "promedio_mayor_n" : valor ["nombre"],
        "promedio_mayor_a" : valor ["apellido"]
    }

    return datos_prom

def informar_mayor_prom (datos:list):

    primer = True
    
    for e_estudiantes in datos:
            
        if primer == True:

            try:
                datos_prom = asignar_valores_prom (e_estudiantes)
                primer = False

            except KeyError:
                promediar_notas (datos)
                datos_prom = asignar_valores_prom (e_estudiantes)
                primer = False

        elif e_estudiantes ["promedio"] > datos_prom ["promedio_mayor"]:
            datos_prom = asignar_valores_prom (e_estudiantes)
            

    print (f"El estudiante con mayor promedio se llama {datos_prom ["promedio_mayor_n"]} {datos_prom ["promedio_mayor_a"]}, y su promedio es de {datos_prom ["promedio_mayor"]}.")
