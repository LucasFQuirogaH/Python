# %% [markdown]
# # Funciones
# ## Retroceder Nunca, Rendirse Jamas..
# **Corriendo...**
from vigilante import vigilar
import csv
import formato_tabla
import informe
import fileparse
from lote import Lote
from camion import Camion
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0 , 1 , 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows
#--------------------------------------------------------------------
def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
#--------------------------------------------------------------------
def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]
#--------------------------------------------------------------------
def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
#--------------------------------------------------------------------
def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila['nombre'] in nombres:
            yield fila
#--------------------------------------------------------------------
def imprimir_informe(filas , formateador):
# Imprime adecuadamente una tabla de una lista de tuplas
# (nombre, cajones, precio, cambio).
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    # separa keys y values
    for fila in filas:
        rowrowdata = list(fila.values())
        rowdata = [ rowrowdata[0], str(rowrowdata[1]), str(rowrowdata[2]) ]
        formateador.fila(rowdata)
#--------------------------------------------------------------------
def leer_camion(nom_archivo):
    with open(nom_archivo) as file:
        camiondicts = fileparse.parse_csv(file , select=['nombre','cajones','precio'] , types=[str,int,float])
    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)
#--------------------------------------------------------------------
def ticker (camion_file, log_file, fmt):
    camion = leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file))
    filas = filtrar_datos(filas, camion)
    # fmt = "txt"
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(filas , formateador)
    return None
def main():
    ticker("C:\Python/Unsam Python/Data/camion.csv" , "C:\Python/Unsam Python/Data/mercadolog.csv" , "txt" )

if __name__ is "__main__":
    main()
