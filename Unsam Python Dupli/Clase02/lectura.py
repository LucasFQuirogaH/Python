# %%
import csv
with open('..\Data\camion.csv' , 'rt') as f:
    Lectura = csv.reader(f) #Lee en formato arreglo para trabajar con partes
    next(Lectura) #Se queda con las cabeceras
    suma = 0
    for line in Lectura:
        suma = suma + float(line[1]) * float(line[2])
    print(suma)
# %%
import csv
with open('..\Data\camion.csv' , 'rt') as f:
    Lectura = csv.reader(f) #Lee en formato arreglo para trabajar con partes
    next(Lectura) #Se queda con las cabeceras
    suma = 0
    for line in Lectura:
        if line[0] == 'Naranja':
            print(f'El precio de la naranja es: {line[2]}')
            break
# %%
