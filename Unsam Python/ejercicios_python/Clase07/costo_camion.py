"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para llamarlo a traves de a consola
Ing.Lucas F. Quiroga H. Fecha: 23/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%
from informe import leer_camion
import fileparse
import sys
sys.argv # ['informe.py, 'camion.csv', 'precios.csv']
import csv

# Funciones ---------------------------------------------------------------------------------------------------
## Funcion: Costo camion. -------------------------------------------------------------------------------------
# %%
def costo_camion(archivo):
# Lee el archivo camion
    CamionLeido = leer_camion(archivo)

## Funcion principal: Main ------------------------------------------------------------------------------------
# %%
def main(parametros):
# El main como programa principal
    archivo = ""
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion')
    archivo = sys.argv[1]
    costo_camion(archivo)

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main(sys.argv)

# C:\Python\Unsam Python\ejercicios_python\Clase07>python -i costo_camion.py camion

# y desde consola de python:
# import costo_camion
# costo_camion.main(["costo_camion.py" , "camion"])


