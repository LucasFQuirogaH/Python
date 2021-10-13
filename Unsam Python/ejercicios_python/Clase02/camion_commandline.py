"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 2.10: Ejecución desde la línea de comandos con parámetros
En el programa costo_camion.py, el nombre del archivo de entrada '../Data/camion.csv' fue escrito en el código.

# costo_camion.py
import csv

def costo_camion(nombre_archivo):
    ...
    # Tu código
    ...

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
Esto está bien para ejercitar, pero en un programa real probablemente no harías eso ya que querrías una mayor flexibilidad.
Una posibilidad es pasarle al programa el nombre del archivo que querés procesar como un parámetro cuando lo llamás desde la línea de comandos.

Copiá el contenido de costo_camion.py a un nuevo archivo llamado camion_commandline.py que incorpore la lectura de parámetros por línea de comando
según la sugerencia del siguiente ejemplo:

# camion_commandline.py
import csv
import sys

def costo_camion(nombre_archivo):
    ...
    # Tu código
    ...

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
sys.argv es una lista que contiene los argumentos que le pasamos al script al momento de llamarlo desde la línea de comandos (si es que le pasamos alguno).
Por ejemplo, desde una terminal de Unix (en Windows es similar), para correr nuestro programa y que procese el mismo archivo podríamos escribir:

bash $ python3 camion_commandline.py ../Data/camion.csv
Costo total: 47671.15
bash $
O con el archivo missing.csv:

bash $ python3 camion_commandline.py ../Data/missing.csv
...
Costo total: 30381.15
bash $
Si no le pasamos ningún archivo, va a mostrar el resultado para camion.csv porque lo indicamos con la línea nombre_archivo = '../Data/camion.csv'.

Guardá tu programa en el archivo camion_commandline.py para entregar al final de la clase.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Funcion  --------------------------------------------------------------
def costo_camion(archivo):
    import csv
    Nombre ="C:\Python/Unsam Python/Data/" + archivo + ".csv"
    try:
        with open(Nombre , "r" , encoding="utf8") as Creacion:
            Total = 0
            Lectura = csv.reader(Creacion)
            next(Creacion)
            for Linea in Lectura:
                Total = Total + (float(Linea[1]) * float(Linea[2]))
        print(f"El total es: {Total}")
    except ValueError:
        print("Existe un problema con el archivo selecionado")
    except FileNotFoundError:
        print("El archivo no se encuentra en el directorio")
    except IndexError:
        print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")

csv
# Main  -----------------------------------------------------------------
import sys
archivo=""
if len(sys.argv) == 2:
    archivo = sys.argv[1]
else:
    archivo = "camion"
costo_camion(archivo)
# Profesor : Tenga en cuenta la linea 56 donde la ruta puede variar en su pc para correr el script