"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 3.8: Un ejemplo práctico de enumerate()
Recordá que el archivo Data/missing.csv contiene datos sobre los cajones de un camión, pero tiene algunas filas que faltan.
Usando enumerate(), modificá tu programa costo_camion.py de forma que imprima un aviso (warning) cada vez que encuentre una fila incorrecta.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# # Funcion  --------------------------------------------------------------
# def costo_camion(archivo):
#     import csv
#     Nombre ="Data/" + archivo + ".csv"
#     try:
#         with open(Nombre , "r" , encoding="utf8") as Creacion:
#             Total = 0
#             Lectura = csv.reader(Creacion)
#             next(Lectura)
#             for indice , Linea in enumerate(Lectura, start=1):
#                 try:
#                     Total = Total + (float(Linea[1]) * float(Linea[2]))
#                 except ValueError:
#                     print("Existe un problema con el archivo selecionado")
#                     print(f"El mismo se encuentra en la fila: {indice}")            
#         print(f"El total es: {Total}")
#     except FileNotFoundError:
#         print("El archivo no se encuentra en el directorio")
#     except IndexError:
#         print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
        

## Main  -----------------------------------------------------------------
# while(1):
#     archivo = input("Ingrese el nombre del archivo para calcular el valor total de la carga: ")
#     costo_camion(archivo)

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 3.9: La función zip()
En el archivo Data/camion.csv, la primera línea tiene los encabezados de las columnas.
En los códigos anteriores la descartamos.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Funcion  --------------------------------------------------------------
def costo_camion(archivo):
    encabezados = []
    Total = 0.0
    import csv
    Nombre ="Data/" + archivo + ".csv"
    try:
        with open(Nombre , "r" , encoding="utf8") as Creacion:
            Lectura = csv.reader(Creacion)
            encabezados = next(Lectura)
            for indice , Linea in enumerate(Lectura, start=1):
                try:
                    ListaDeDiccionario = dict(zip(encabezados, Linea)) # ----- Apareo 
                    Total = Total + (float(ListaDeDiccionario["cajones"]) * float(ListaDeDiccionario["precio"]))
                except ValueError:
                    print("Existe un problema con el archivo selecionado")
                    print(f"El mismo se encuentra en la fila: {indice}")            
        print(f"El total es: {Total}")
    except FileNotFoundError:
        print("El archivo no se encuentra en el directorio")
    except IndexError:
        print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
        

# Main  -----------------------------------------------------------------
while(1):
    archivo = input("Ingrese el nombre del archivo para calcular el valor total de la carga: ")
    costo_camion(archivo)
