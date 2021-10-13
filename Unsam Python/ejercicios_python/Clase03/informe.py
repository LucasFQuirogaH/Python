"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#############################################################################  Preliminares  #################################################################################
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# # Funcion  --------------------------------------------------------------
# def leer_camion(archivo):
#     import csv
#     ElNombre = ""
#     Total = 0
#     Nombre ="Data/" + archivo + ".csv"
#     try:
#         with open(Nombre , "r" , encoding="utf8") as Creacion:
#             camion = []
#             tupla = tuple()
#             Lectura = csv.reader(Creacion)
#             next(Creacion)
#             for Linea in Lectura:
#                 tupla = (Linea[0] , int(Linea[1]) , float(Linea[2]))
#                 Total = Total + (float(Linea[1]) * float(Linea[2]))
#                 camion.append(tupla)
#         print(f"El contenido del camion es: {camion}")
#         print(f"El total es: {Total}")
#     except ValueError:
#         print("Existe un problema con el archivo selecionado")
#     except FileNotFoundError:
#         print("El archivo no se encuentra en el directorio")
#     except IndexError:
#         print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
        
# # Main  -----------------------------------------------------------------
# archivo = "camion"
# leer_camion(archivo)
"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 2.16: Lista de diccionarios
Tomá la función que escribiste en el ejercicio anterior y modificala para representar cada cajón del camión con un diccionario en vez de una tupla.
En este diccionario usá los campos "nombre", "cajones" y "precio" para representar las diferentes columnas del archivo de entrada.

Experimentá con esta función nueva igual que en el ejercicio anterior.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# # Funcion  --------------------------------------------------------------
# def leer_camion(archivo):
#     import csv
#     from pprint import pprint
#     Total = 0
#     Diccionario = {}
#     cabecera =""
#     camion =[]
#     Nombre ="C:\Python/Unsam Python/Data/" + archivo + ".csv"
#     try:
#         with open(Nombre , "r" , encoding="utf8") as Creacion:
#             Lectura = csv.reader(Creacion)
#             cabecera = next(Lectura)
#             for Linea in Lectura:
#                 Diccionario[cabecera[0]] = Linea[0]
#                 Diccionario[cabecera[1]] = Linea[1]
#                 Diccionario[cabecera[2]] = Linea[2]
#                 camion.append(Diccionario)
#                 Diccionario = {}
#                 Total = Total + (float(Linea[1]) * float(Linea[2]))
#             pprint(camion)
#         print(f"El total es: {Total}")
#     except ValueError:
#         print("Existe un problema con el archivo selecionado")
#     except FileNotFoundError:
#         print("El archivo no se encuentra en el directorio")
#     except IndexError:
#         print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
        
# # Main  -----------------------------------------------------------------
# archivo = "camion"
# leer_camion(archivo)
"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##################################################################################  Bueno Vamos  ####################################################################################
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 2.18: Balances
Supongamos que los precios en camion.csv son los precios pagados al productor de frutas mientras que los precios en precios.csv son los precios de venta
en el lugar de descarga del camión.

Ahora vamos calcular el balance del negocio: juntá todo el trabajo que hiciste recién en tu programa informe.py (usando las funciones leer_camion() y leer_precios())
y completá el programa para que con los precios del camión (Ejercicio 2.16) y los de venta en el negocio (Ejercicio 2.17)
calcule lo que costó el camión, lo que se recaudó con la venta, y la diferencia. ¿Hubo ganancia o pérdida?
El programa debe imprimir por pantalla un balance con estos datos.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Funciones  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def leer_camion(archivo):
    import csv
    from pprint import pprint
    global Total
    Total = 0
    UnDiccionario = {}
    cabecera =""
    camion =[]
    Nombre ="Data/" + archivo + ".csv"# <---------- Profesor: Considere un cambio de ruta para correr el script en su pc
    try:
        with open(Nombre , "r" , encoding="utf8") as Creacion:
            Lectura = csv.reader(Creacion)
            cabecera = next(Lectura)
            for Linea in Lectura:
                UnDiccionario = dict(zip(cabecera, Linea))
                Total = Total + (float(UnDiccionario["cajones"]) * float(UnDiccionario["precio"]))
                camion.append(UnDiccionario)
                UnDiccionario = {}
        print(f"El costo del camion es: {Total}")
    except ValueError:
        print("Existe un problema con el archivo selecionado")
    except FileNotFoundError:
        print("El archivo no se encuentra en el directorio")
    except IndexError:
        print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
    return (camion)


def leer_precios(archivo):
    import csv
    from pprint import pprint
    OtroDicionario ={}
    Precios = {}
    Cabecera = []
    Nombre ="Data/" + archivo + ".csv"
    with open(Nombre, "r" , encoding="utf8") as creacion:
        Lectura = csv.reader(creacion)
        Cabecera = ["nombre" , "precio"]
        for Linea in Lectura:
            try:
                if len(Linea) == len(Cabecera):
                    OtroDicionario = dict(zip(Cabecera,Linea)) 
                    Precios[OtroDicionario["nombre"]] = OtroDicionario["precio"]
            except IndexError:
                print("### Se omitieron algunas filas con datos faltantes ###")
    return(Precios)
        
def calculo_de_costos(CamionLeido , PrecioLeido):
    TotalCostos = 0
    PrecioLeidoKeys = list(PrecioLeido.keys())
    PrecioLeidoValues = list(PrecioLeido.values())
#---------------------------------------------------------------------------------------------------------------    
    for LineaCamion in CamionLeido: #------------------Es una lista con diccionarios dentro        
        for indice , Linea in enumerate(PrecioLeidoKeys):#--------Es un diccionario enorme
            if Linea == LineaCamion["nombre"]:
                TotalCostos= TotalCostos + float(LineaCamion["cajones"]) * float(PrecioLeidoValues[indice])
    print(f"Total de costos vendidos en el lugar es : {TotalCostos}")
    print(f"Hubo una ganancia de: {round((TotalCostos - Total), 2)}")
        
# Main  --------------------------------------------------------------------------------------------------------
CamionLeido = leer_camion("camion")
print("\n")
PrecioLeido = leer_precios("precios")
print("\n")
calculo_de_costos(CamionLeido , PrecioLeido )

"""----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Sr. Profesor, considere en todo momento la ruta desde donde se leen los archivos csv para que el programa funcione correctamente. El archivo se encuentra funcionando
correctamente. ATTE. Lucas Quiroga
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
