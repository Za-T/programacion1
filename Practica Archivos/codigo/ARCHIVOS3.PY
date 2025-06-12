#GENERAR UN ARCHIVO json
#dump = indenta el archivo en formato json
#ensure_ascii se usa para asegurarse que todos los caracteres sean un ascii real. 
#pero se le puede dar un valor de false para que no modifique la string dada

import json
data = {}
data['clientes'] = []

data['clientes'].append({ 'nombre': 'Juan', 'edad': 27})
data['clientes'].append({ 'nombre': 'Ana', 'edad': 26})

with open('data_generado.json', 'w') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

