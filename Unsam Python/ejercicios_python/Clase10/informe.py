"""------------------------------------------------------------------------------------------------------------
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%
import fileparse
from lote import Lote
import formato_tabla
import sys
from camion import Camion

# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Leer camion -------------------------------------------------------------------------------------
def leer_camion(nom_archivo):
# Lee un archivo de lotes en un camión
# y lo devuelve como lista de diccionarios con claves
# nombre, cajones, precio.
    Nombre = "C:\Python/Unsam Python/Data/" + nom_archivo + ".csv"
    with open(Nombre) as file:
        camiondicts = fileparse.parse_csv(file , select=['nombre','cajones','precio'] , types=[str,int,float])
    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)
## Funciones: Leer Precios ------------------------------------------------------------------------------------
# %%
def leer_precios(nom_archivo):
# Lee un archivo CSV con data de precios
# y lo devuelve como un diccionario
# con claves nombres y con sus precios como valores
    Nombre = 'C:\Python/Unsam Python/Data/' + nom_archivo + '.csv'
    with open(Nombre , encoding = "utf8") as lines:
        precios = dict(fileparse.parse_csv(lines, types = [str,float], has_headers = False))
    ListaDeFrutas = list(precios.keys())
    ListaDePrecios = list(precios.values())
    precios = [ Lote(ListaDeFrutas[i] , 0 , ListaDePrecios[i]) for i in range(len(ListaDeFrutas))]
    return precios

## Funciones: Hacer informe -----------------------------------------------------------------------------------
# %%
def hacer_informe(camion, precios):
# Crea una lista de tuplas (nombre, cajones, precio, cambio)
# dada una lista de lotes en un camión y un diccionario de precios nuevos.
    filas = []
    for c in camion:
        precio_orig = c.precio
        for p in precios:
            if p.nombre == c.nombre:
                cambio = p.precio - c.precio
                reg = (c.nombre , c.cajones , c.precio , cambio)
                filas.append(reg)
    return filas

## Funciones: Imprimir informe --------------------------------------------------------------------------------
# %%
def imprimir_informe(data_informe , formateador):
# Imprime adecuadamente una tabla de una lista de tuplas
# (nombre, cajones, precio, cambio).
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)

## Funciones: Informe Camion ----------------------------------------------------------------------------------
# %%
def informe_camion(archivo_camion, archivo_precios , fmt = "txt"):
# Crea un informe a partir de un archivo de camión y otro de precios de venta.
# Lee data files
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la información del informe
    data_informe = hacer_informe(camion, precios)

    # Lo imprime
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe , formateador)
#%%
def main(args):
    if (len(args) > 4) or (len(args) < 3):
        raise SystemExit('Uso: %s archivo_camion archivo_precios' % args[0])
    elif len(args) == 3:
        informe_camion(args[1], args[2])
    else:
        informe_camion(args[1], args[2] , args[3])
#%%
if __name__ == '__main__':
    main(sys.argv)
