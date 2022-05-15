"""------------------------------------------------------------------------------------------------------------
Parse modificado en clase8 para que le pases solo el puntero, no el nombre del archivo.
Ing.Lucas F. Quiroga H. Fecha: 22/04/2021 Retroceder nunca, rendirse jamas.
------------------------------------------------------------------------------------------------------------"""

# Import
# %%
import csv
import pprint

# Funciones ---------------------------------------------------------------------------------------------------
## Funcion: Lectura completa de los arboles. ------------------------------------------------------------------
# %%
def parse_csv(file , select = None , types = None , has_headers = False):
# lee un archivo CSV y arma una lista de diccionarios a partir del contenido del archivo CSV. La función aísla
# al programador de los múltiples pequeños pasos necesarios para abrir un archivo, "envolverlo" con el módulo csv,
# ignorar líneas vacías, y demás minucias.
    filas = csv.reader(file)
    registros = []
    encabezados = []
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
    elif (has_headers == False) and (select != None):
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    else:
        for i , fila in enumerate(filas):
            if not fila:
                continue
            elif types:
                try:
                    fila = [func(val) for func, val in zip(types, fila)]
                except ValueError:
                    # print (f"Fila {i} no se proceso")
                    # print("Motivo: Faltante de datos validos para procesar.")
                    continue
            registros.append(tuple(fila))
    return registros

## FUNCIONES FUNCION MAIN ------------------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    # %%
    camion = parse_csv("C:\Python/Unsam Python/Data/missing.csv", types = [str, int, float])
    print(camion)
    # %%
    # precios = parse_csv('C:\Python/Unsam Python/Data/precios.csv', types=[str,float], has_headers=False)
    # pprint.pprint(precios)
    # %%
    # camion = parse_csv("C:\Python/Unsam Python/Data/missing.csv", types = [str, int, float])
    # print(camion)

# Main  ------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()
