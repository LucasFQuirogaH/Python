# vigilante.py
#--------------------------------------------------------------------
# %%
#
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
# f = open('C:\Python/Unsam Python/Data/mercadolog.csv')
# f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
# while True:
#     line = f.readline() # Se usa para leer las ultimas lineas del archivo, porque se va generando en tiempo real
#     if line == '':
#         time.sleep(0.5)   # Esperar un rato y
#         continue          # vuelve al comienzo del while
#     fields = line.split(',')
#     nombre = fields[0].strip('"')
#     precio = float(fields[1])
#     volumen = int(fields[2])
#     if volumen > 1000:
#         print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
#--------------------------------------------------------------------
# %%
#
# def vigilar(Direccion):
# #Contrato:
# # Precondicion:
# # Poscondicion:
#     import os
#     import time
#     f = open(Direccion)
#     f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
#     while True:
#         line = f.readline() # Se usa para leer las ultimas lineas del archivo, porque se va generando en tiempo real
#         if line == '':
#             time.sleep(0.5)   # Esperar un rato y
#             continue          # vuelve al comienzo del while
#         fields = line.split(',')
#         nombre = fields[0].strip('"')
#         precio = float(fields[1])
#         volumen = int(fields[2])
#         if volumen > 1000:
#             yield f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}'
#--------------------------------------------------------------------
# %%
#
# for line in vigilar('C:\Python/Unsam Python/Data/mercadolog.csv'):
#     print(line)

# %%
# 10.6
def vigilar(Direccion):
    import os
    import time
    f = open(Direccion)
    f.seek(0, os.SEEK_END)   # Mover el índice 0 posiciones desde el EOF
    while True:
        line = f.readline() # Se usa para leer las ultimas lineas del archivo, porque se va generando en tiempo real
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        yield line
# %%
#
if __name__ == '__main__':
    import informe
    camion = informe.leer_camion ("camion") # Mi leer ca
    for line in vigilar('C:\Python/Unsam Python/Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])
        if nombre in camion:
            print(f'{nombre:>10s} {precio:>10.2f} {volumen:>10d}')
# %%
