"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
########################################################################  Preliminares de la clase 02  #############################################################################
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# import csv
# creacion = open("Data/camion.csv" , "r" , encoding="utf8")
# leidos = csv.reader(creacion) #Leyo y ya realizo el split
# cabeceras = next(leidos)
# print(cabeceras)

# for linea in leidos:
#     print(linea)

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##################################################################################  Bueno Vamos  ####################################################################################
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 2.2: Lectura de un archivo de datos
Ahora que sabés leer un archivo, escribamos un programa que haga un cálculo simple con los datos leídos.

Las columnas en camion.csv corresponden a un nombre de fruta, una cantidad de cajones cargados en el camión, y un precio de compra por cada cajón de ese grupo.
Escribí un programa llamado costo_camion.py que abra el archivo, lea las líneas, y calcule el precio pagado por los cajones cargados en el camión.

Ayuda: para interpretar un string s como un número entero, usá int(s). Para leerlo como punto flotante, usá float(s).

Tu programa debería imprimir una salida como la siguiente:

Costo total 47671.15
Acordate de guardar tu archivo en el directorio Clase02; vamos a volver a trabajar sobre él.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# with open("Data/camion.csv", "r" , encoding="utf8") as Creacion:
#     Total = 0
#     cabeceras = next(Creacion)
#     for Linea in Creacion:
#         EnLista = Linea.split(",")
#         # print(EnLista[2])
#         Total = Total + (float(EnLista[1]) * float(EnLista[2]))
# print(f"El total es: {Total}")

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 2.6: Transformar un script en una función
Transformá el programa costo_camion.py (que escribiste en el Ejercicio 2.2 de la sección anterior) en una función costo_camion(nombre_archivo).
Esta función recibe un nombre de archivo como entrada, lee la información sobre los cajones que cargó el camión
y devuelve el costo de la carga de frutas como una variable de punto flotante.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# # Funcion  --------------------------------------------------------------
# def costo_camion(archivo):
#     Nombre ="Data/" + archivo + ".csv"
#     try:
#         with open(Nombre , "r" , encoding="utf8") as Creacion:
#             Total = 0
#             next(Creacion)
#             for Linea in Creacion:
#                 EnLista = Linea.split(",")
#                 Total = Total + (float(EnLista[1]) * float(EnLista[2]))
#         print(f"El total es: {Total}")
#     except ValueError:
#         print("Existe un problema con el archivo selecionado")
        

# # Main  -----------------------------------------------------------------
# while(1):
#     archivo = input("Ingrese el nombre del archivo para calcular el valor total de la carga: ")
#     costo_camion(archivo)

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 2.9: Funciones de la biblioteca
Python viene con una gran biblioteca estándar de funciones útiles.
En este caso el módulo csv podría venirnos muy bien. Podés usarlo cada vez que tengas que leer archivos CSV. Acá va un ejemplo de cómo funciona..
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Funcion  --------------------------------------------------------------
def costo_camion(archivo):
    import csv
    Nombre ="Data/" + archivo + ".csv"
    try:
        with open(Nombre , "r" , encoding="utf8") as Creacion:
            print(Creacion)
            Total = 0
            Lectura = csv.reader(Creacion)
            print(Lectura)
            next(Lectura)
            for Linea in Lectura:
                print(Linea)
                Total = Total + (float(Linea[1]) * float(Linea[2]))
        print(f"El total es: {Total}")
    except ValueError:
        print("Existe un problema con el archivo selecionado")
    except FileNotFoundError:
        print("El archivo no se encuentra en el directorio")
    except IndexError:
        print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
        

# Main  -----------------------------------------------------------------
while(1):
    archivo = input("Ingrese el nombre del archivo para calcular el valor total de la carga: ")
    costo_camion(archivo)

# Aqui modifique el script para que pida por consola al operador el nombre del archivo, asi comete equivocaciones segun excepciones