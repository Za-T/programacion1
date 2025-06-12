# Convierte el texto en binario
texto = "Convertimos el texto en una secuencia de bytes utilizando el método encode() con la codificación UTF-8"
datos_binarios = texto.encode('utf-8')  # UTF-8 es una codificación común para texto

with open("data_salida.bin","wb") as archivo:
    archivo.write(datos_binarios)
