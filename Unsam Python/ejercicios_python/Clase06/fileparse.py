"""------------------------------------------------------------------------------------------------------------
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas.
------------------------------------------------------------------------------------------------------------"""
# Funciones ---------------------------------------------------------------------------------------------------
## Funcion: Lectura completa de los arboles. ------------------------------------------------------------------
#%%
# def parse_csv(nombre_archivo , select = None):
# # Parsea un archivo CSV en una lista de registros.
# # Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una
# # lista de nombres de las columnas a considerar.
#     with open(nombre_archivo) as f:
#         filas = csv.reader(f)
#         # Lee los encabezados del archivo
#         encabezados = next(filas)
#         # Si se indicó un selector de columnas,
#         # buscar los índices de las columnas especificadas.
#         # Y en ese caso achicar el conjunto de encabezados para diccionarios
#         if select:
#             indices = [encabezados.index(nombre_columna) for nombre_columna in select]
#             encabezados = select
#         else:
#             indices = []
#         registros = []
#         for fila in filas:
#             if not fila:    # Saltear filas vacías
#                 continue
#             # Filtrar la fila si se especificaron columnas
#             if indices:
#                 fila = [fila[index] for index in indices]
#             # Armar el diccionario
#             registro = dict(zip(encabezados, fila))
#             registros.append(registro)
#     return registros

# Main  --------------------------------------------------------------------------------------------------------
# %%
# import csv
# import pprint
# %%
# camion = parse_csv('C:\Python/Unsam Python/Data/camion.csv')
# pprint.pprint(camion)
# %%
# cajones_retenidos = parse_csv('C:\Python/Unsam Python/Data/camion.csv', select = ['nombre','cajones'])
# pprint.pprint(cajones_retenidos)
# %%





# 6.8

# Import
# %%
# import csv
# import pprint

# Funciones ---------------------------------------------------------------------------------------------------
## Funcion: Lectura completa de los arboles. ------------------------------------------------------------------
# %%
# def parse_csv(nombre_archivo , select = None, types = None):
#     with open(nombre_archivo) as f:
#         filas = csv.reader(f)
#         encabezados = next(filas)
#         if select and types:
#             indices = [encabezados.index(nombre_columna) for nombre_columna in select]
#             encabezados = select
#         else:
#             indices = []
#             registros = []
#         for fila in filas:
#             if not fila:    # Saltear filas vacías
#                 continue
#             if indices:
#                 fila = [fila[index] for index in indices]
#             if types:
#                 fila = [func(val) for func, val in zip(types, fila)]
#             registro = dict(zip(encabezados, fila))
#             registros.append(registro)
#     return registros

# Main  --------------------------------------------------------------------------------------------------------
# %% 6.8
# camion = parse_csv('C:\Python/Unsam Python/Data/camion.csv', types=[str, int, float])
# pprint.pprint(camion)




# 6.9

# Import
# %%
import csv
import pprint

# Funciones ---------------------------------------------------------------------------------------------------
## Funcion: Lectura completa de los arboles. ------------------------------------------------------------------
# %%
def parse_csv(nombre_archivo , select = None , types = None , has_headers = False):
    with open(nombre_archivo , "rt" , encoding="utf8") as f:
        filas = csv.reader(f)
        registros = []
        if has_headers:
            encabezados = next(filas)
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            else:
                indices = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                    registro = dict(zip(encabezados, fila))
                    registros.append(registro)
        else:
            for fila in filas:
                if not fila:
                    continue
                elif types:
                    fila = [func(val) for func, val in zip(types, fila)]
                registros.append(tuple(fila))
    return registros

# Main  --------------------------------------------------------------------------------------------------------
# %%
precios = parse_csv('C:\Python/Unsam Python/Data/precios.csv', types=[str,float], has_headers=False)
pprint.pprint(precios)
# %%
camion = parse_csv('C:\Python/Unsam Python/Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float] , has_headers = True)
pprint.pprint(camion)
# %%
