# informe.py

import fileparse
import lote

#import lote
def leer_camion(nom_archivo):
# Lee un archivo de lotes en un camión
# y lo devuelve como lista de diccionarios con claves
# nombre, cajones, precio.
    Nombre = 'C:\Python/Unsam Python/Data/' + nom_archivo + '.csv'
    with open(Nombre) as lineas:
        camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    camion = [ lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return camion

#--------------------------------------------------------------------
# %%
#
def leer_precios(nom_archivo):
# Lee un archivo CSV con data de precios
# y lo devuelve como un diccionario
# con claves nombres y con sus precios como valores
    Nombre = 'C:\Python/Unsam Python/Data/' + nom_archivo + '.csv'
    with open(Nombre , encoding = "utf8") as lines:
        precios = dict(fileparse.parse_csv(lines, types = [str,float], has_headers = False))
    ListaDeFrutas = list(precios.keys())
    ListaDePrecios = list(precios.values())
    precios = [ lote.Lote(ListaDeFrutas[i] , 0 , ListaDePrecios[i]) for i in range(len(ListaDeFrutas))]
    return precios

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
#%%
def imprimir_informe(data_informe):
# Imprime adecuadamente una tabla de una lista de tuplas
# (nombre, cajones, precio, cambio).
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for fila in data_informe:
        print('%10s %10d %10.2f %10.2f' % fila)

def informe_camion(archivo_camion, archivo_precios):
    '''
    Crea un informe a partir de un archivo de camión y otro de precios de venta.
    '''
    # Lee data files
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la información del informe
    data_informe = hacer_informe(camion, precios)

    # Lo imprime
    imprimir_informe(data_informe)
#%%
def main(args):
    if len(args) != 3:
        raise SystemExit('Uso: %s archivo_camion archivo_precios' % args[0])
    informe_camion(args[1], args[2])
#%%
if __name__ == '__main__':
    import sys
    main(sys.argv)
