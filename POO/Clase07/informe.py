"""------------------------------------------------------------------------------------------------------------
Modificacion del archivo informe para hacer que se llame facilmente por consola agregando a la misma linea
los argumentos necesarios
Ing.Lucas F. Quiroga H. Fecha: 23/04/2021.
------------------------------------------------------------------------------------------------------------"""
# Import
import fileparse
import sys
sys.argv # ['informe.py, 'camion.csv', 'precios.csv']

# Funciones ---------------------------------------------------------------------------------------------------
## Funcion: Leer camion. --------------------------------------------------------------------------------------
# %%
def leer_camion(archivo):
# Lee un archivo csv con el contenido de un camion.
    import csv
    Total = 0
    camion =[]
    camion = fileparse.parse_csv(archivo , select = ['nombre', 'cajones', 'precio'], types = [str, int, float] , has_headers = True)
    Total = sum(float(Linea["cajones"]) * (Linea["precio"]) for Linea in camion)
    print()
    print(f"El costo del camion es: {Total:^10.2f}")
    return (camion)

## Funcion: Leer precios. -------------------------------------------------------------------------------------
# %%
def leer_precios(archivo):
# Lee los precios a partir de un archivo csv de precios
    import csv
    from pprint import pprint
    Precios = {}
    Precios = fileparse.parse_csv(archivo , types=[str,float], has_headers=False)
    return(Precios)

## Funcion: Calculo de costos. --------------------------------------------------------------------------------
# %%
def calculo_de_costos(CamionLeido , PrecioLeido):
# Genera el calculo de los costos del camion
# Y la ganancia que se obtiene del mismo a otro precio
    TotalCostos = 0.0
    Total = 0.0
    PrecioLeidoKeys = []
    PrecioLeidoValues = []
    PrecioLeidoKeys , PrecioLeidoValues = map(list, zip(*PrecioLeido))
    for LineaCamion in CamionLeido: #------------------Es una lista con diccionarios dentro
        for indice , Linea in enumerate(PrecioLeidoKeys):#--------Es un diccionario enorme
            if Linea == LineaCamion["nombre"]:
                TotalCostos= TotalCostos + float(LineaCamion["cajones"]) * float(PrecioLeidoValues[indice])
                Total= Total + float(LineaCamion["cajones"]) * float(LineaCamion["precio"])
    print("\n")
    print(f"Total de costos vendidos en el lugar es : {TotalCostos:^10.2f}")
    print("\n")
    print(f"Hubo una ganancia de: {(TotalCostos - Total):^10.2f}")
    print("\n")
    return PrecioLeidoKeys, PrecioLeidoValues

## Hacer informes. --------------------------------------------------------------------------------------------
# %%
def hacer_informe(CamionLeido, PrecioLeidoKeys, PrecioLeidoValues):
# Esta funcion recibe el camion leido como una lista de diccionarios y 2 listas mas que representan
# la lista completa de precios de venta, separadas con frutas y precios.
    Nombres = []
    Cajones = []
    Precios = []
    Cambios = []
    informe = ()
    for Linea in CamionLeido:
        Nombres.append(Linea['nombre'])
        Cajones.append((int(Linea['cajones'])))
        Precios.append(float(Linea['precio']))
        for i , key in enumerate(PrecioLeidoKeys):
            if key == Linea['nombre']:
                Cambios.append(round((float(PrecioLeidoValues[i]) - float(Linea['precio'])) , 2))
                break
            informe = tuple(zip(Nombres , Cajones , Precios , Cambios))
    return informe

## Funcion: Lectura completa de los arboles. ------------------------------------------------------------------
# %%
def imprimir_informe(informe):
# Esta funcion imprime una tabla de informe de costos de frutas como asi tambien cajones que se vendieron
# y las ganancias.
    Headers = ("Nombre" , "Cajones" , "Precios" , "Cambio")
    ListaHeaders = list(Headers)
    print(f"{ListaHeaders[0]:>10s} {ListaHeaders[1]:>10s} {ListaHeaders[2]:>10s} {ListaHeaders[3]:>10s}")
    print(f"-----------------------------------------------")
    for tupla in informe:
        print(f"{tupla[0]:>10s} {tupla[1]:>10d} {tupla[2]:>10.2f} {tupla[3]:>10.2f}")
    return None

## Funciones: Informe completo del camion ----------------------------------------------------------------------
# %%
def informe_camion(camion , precios):
# Funcion que corre en programa entero
    CamionLeido = leer_camion(camion)
    #CamionLeido = fileparse.parse_csv('C:\Python/Unsam Python/Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float] , has_headers = True)
    print("\n")
    PrecioLeido = leer_precios(precios)
    #PrecioLeido = fileparse.parse_csv('C:\Python/Unsam Python/Data/precios.csv', types=[str,float], has_headers=False)
    print("\n")
    PrecioLeidoKeys, PrecioLeidoValues  = calculo_de_costos(CamionLeido , PrecioLeido)
    informe = hacer_informe(CamionLeido, PrecioLeidoKeys, PrecioLeidoValues)
    imprimir_informe(informe)
    return None

## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def main(parametros):
# El main como programa principal
    archivo1 = ""
    archivo2 = ""
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    archivo1 = sys.argv[1]
    archivo2 = sys.argv[2]
    informe_camion(archivo1 , archivo2)
# Main  --------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main(sys.argv)

# C:\Python\Unsam Python\ejercicios_python\Clase07>python -i informe.py camion
# y desde consola de python:
# import informe
# informe.main(["informe.py" , "camion" , "precios"])