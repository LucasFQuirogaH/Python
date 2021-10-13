"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Funcion para buscar el precio de lo que pidas
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Funciones ---------------------------------------------------------
def leer_precios(archivo):
    import csv
    from pprint import pprint
    Precios ={}
    Nombre ="C:\Python/Unsam Python/Data/" + archivo + ".csv"
    with open(Nombre, "r" , encoding="utf8") as creacion:
        Lectura = csv.reader(creacion)
        print(Lectura)
        for Linea in Lectura:
            try:
                Precios[Linea[0]] = Linea[1]
            except IndexError:
                print("### Se omitieron algunas filas con datos faltantes ###")
        pprint(Precios)
# Main --------------------------------------------------------------
leer_precios("precios")