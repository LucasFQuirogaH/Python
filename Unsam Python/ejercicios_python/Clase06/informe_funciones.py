"""------------------------------------------------------------------------------------------------------------
Modificacion del archivo informe_funciones.
Ing.Lucas F. Quiroga H. Fecha: 19/04/2021. 
------------------------------------------------------------------------------------------------------------"""
# Funciones ---------------------------------------------------------------------------------------------------
## Funcion: Leer camion. --------------------------------------------------------------------------------------
# def leer_camion(archivo):
# Lee un archivo csv con el contenido de un camion.
    # import csv
    # from pprint import pprint
    # global Total
    # Total = 0
    # UnDiccionario = {}
    # cabecera =""
    # camion =[]
    # Nombre ="Data/" + archivo + ".csv"#<--------------------------------------- Profesor: Considere un cambio de ruta para correr el script en su pc
    # try:
    #     with open(Nombre , "r" , encoding="utf8") as Creacion:
    #         Lectura = csv.reader(Creacion)
    #         cabecera = next(Lectura)
    #         for Linea in Lectura:
    #             UnDiccionario = dict(zip(cabecera, Linea))
    #             Total = Total + (float(UnDiccionario["cajones"]) * float(UnDiccionario["precio"]))
    #             camion.append(UnDiccionario)
    #             UnDiccionario = {}
    #     print(f"El costo del camion es: {Total:^10.2f}")
    # except ValueError:
    #     print("Existe un problema con el archivo selecionado")
    # except FileNotFoundError:
    #     print("El archivo no se encuentra en el directorio")
    # except IndexError:
    #     print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
    # return (camion)

## Funcion: Leer precios. -------------------------------------------------------------------------------------
# def leer_precios(archivo):
# Lee los precios a partir de un archivo csv de precios
    # import csv
    # from pprint import pprint
    # OtroDicionario ={}
    # Precios = {}
    # Cabecera = []
    # Nombre ="Data/" + archivo + ".csv"
    # with open(Nombre, "r" , encoding="utf8") as creacion:
    #     Lectura = csv.reader(creacion)
    #     Cabecera = ["nombre" , "precio"]
    #     for Linea in Lectura:
    #         try:
    #             if len(Linea) == len(Cabecera):
    #                 OtroDicionario = dict(zip(Cabecera,Linea)) 
    #                 Precios[OtroDicionario["nombre"]] = OtroDicionario["precio"]
    #         except IndexError:
    #             print("### Se omitieron algunas filas con datos faltantes ###")
    # return(Precios)

## Funcion: Calculo de costos. --------------------------------------------------------------------------------
# def calculo_de_costos(CamionLeido , PrecioLeido):
# Genera el calculo de los costos del camion
# Y la ganancia que se obtiene del mismo a otro precio
    # TotalCostos = 0.0
    # PrecioLeidoKeys = list(PrecioLeido.keys())
    # PrecioLeidoValues = list(PrecioLeido.values())  
    # for LineaCamion in CamionLeido: #------------------Es una lista con diccionarios dentro        
    #     for indice , Linea in enumerate(PrecioLeidoKeys):#--------Es un diccionario enorme
    #         if Linea == LineaCamion["nombre"]:
    #             TotalCostos= TotalCostos + float(LineaCamion["cajones"]) * float(PrecioLeidoValues[indice])
    # print("\n")
    # print(f"Total de costos vendidos en el lugar es : {TotalCostos:^10.2f}")
    # print("\n")
    # print(f"Hubo una ganancia de: {(TotalCostos - Total):^10.2f}")
    # print("\n")
    # return CamionLeido, PrecioLeidoKeys, PrecioLeidoValues 

## Hacer informes. --------------------------------------------------------------------------------------------
# def hacer_informe(CamionLeido, PrecioLeidoKeys, PrecioLeidoValues):
# Esta funcion recibe el camion leido como una lista de diccionarios y 2 listas mas que representan
# la lista completa de precios de venta, separadas con frutas y precios.
    # Nombres = []
    # Cajones = []
    # Precios = []
    # Cambios = []
    # informe = ()
    # for Linea in CamionLeido:
    #     Nombres.append(Linea['nombre'])
    #     Cajones.append((int(Linea['cajones'])))
    #     Precios.append(float(Linea['precio']))
    #     for i , key in enumerate(PrecioLeidoKeys):
    #         if key == Linea['nombre']:
    #             Cambios.append(round((float(PrecioLeidoValues[i]) - float(Linea['precio'])) , 2))
    #             break
    #         informe = tuple(zip(Nombres , Cajones , Precios , Cambios))
    # return informe

## Funcion: Lectura completa de los arboles. ------------------------------------------------------------------
# def imprimir_informe(informe):
# Esta funcion imprime una tabla de informe de costos de frutas como asi tambien cajones que se vendieron
# y las ganancias.
    # Headers = ("Nombre" , "Cajones" , "Precios" , "Cambio")
    # ListaHeaders = list(Headers)
    # print(f"{ListaHeaders[0]:>10s} {ListaHeaders[1]:>10s} {ListaHeaders[2]:>10s} {ListaHeaders[3]:>10s}")
    # print(f"-----------------------------------------------")
    # for tupla in informe:
    #     print(f"{tupla[0]:>10s} {tupla[1]:>10d} {tupla[2]:>10.2f} {tupla[3]:>10.2f}")
    # return None

# def informe_camion(camion , precios):
# Funcion que corre en programa entero
    # CamionLeido = leer_camion(camion)
    # print("\n")
    # PrecioLeido = leer_precios(precios)
    # print("\n")
    # CamionLeido, PrecioLeidoKeys, PrecioLeidoValues  = calculo_de_costos(CamionLeido , PrecioLeido)
    # informe = hacer_informe(CamionLeido, PrecioLeidoKeys, PrecioLeidoValues)
    # imprimir_informe(informe)
    # return None

# Main  --------------------------------------------------------------------------------------------------------
# informe_camion("camion" , "precios")


"""------------------------------------------------------------------------------------------------------------
Modificacion del archivo informe_funciones.
Ing.Lucas F. Quiroga H. Fecha: 19/04/2021. 
------------------------------------------------------------------------------------------------------------"""
# Import
#import fileparse

# Funciones ---------------------------------------------------------------------------------------------------
## Funcion: Leer camion. --------------------------------------------------------------------------------------
# def leer_camion(archivo):
# # Lee un archivo csv con el contenido de un camion.
#     import csv
#     from pprint import pprint
#     Total = 0
#     UnDiccionario = {}
#     cabecera =""
#     camion =[]
#     Nombre ="Data/" + archivo + ".csv"
#     try:
#         with open(Nombre , "r" , encoding="utf8") as Creacion:
#             Lectura = csv.reader(Creacion)
#             cabecera = next(Lectura)
#             for Linea in Lectura:
#                 UnDiccionario = dict(zip(cabecera, Linea))
#                 Total = Total + (float(UnDiccionario["cajones"]) * float(UnDiccionario["precio"]))
#                 camion.append(UnDiccionario)
#                 UnDiccionario = {}
#         print(f"El costo del camion es: {Total:^10.2f}")
#     except ValueError:
#         print("Existe un problema con el archivo selecionado")
#     except FileNotFoundError:
#         print("El archivo no se encuentra en el directorio")
#     except IndexError:
#         print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
#     return (camion)

## Funcion: Leer precios. -------------------------------------------------------------------------------------
# def leer_precios(archivo):
# # Lee los precios a partir de un archivo csv de precios
#     import csv
#     from pprint import pprint
#     OtroDicionario ={}
#     Precios = {}
#     Cabecera = []
#     Nombre ="Data/" + archivo + ".csv"
#     with open(Nombre, "r" , encoding="utf8") as creacion:
#         Lectura = csv.reader(creacion)
#         Cabecera = ["nombre" , "precio"]
#         for Linea in Lectura:
#             try:
#                 if len(Linea) == len(Cabecera):
#                     OtroDicionario = dict(zip(Cabecera,Linea)) 
#                     Precios[OtroDicionario["nombre"]] = OtroDicionario["precio"]
#             except IndexError:
#                 print("### Se omitieron algunas filas con datos faltantes ###")
#     return(Precios)

## Funcion: Calculo de costos. --------------------------------------------------------------------------------
# def calculo_de_costos(CamionLeido , PrecioLeido):
# # Genera el calculo de los costos del camion
# # Y la ganancia que se obtiene del mismo a otro precio
#     TotalCostos = 0.0
#     Total = 0.0
#     PrecioLeidoKeys = list(PrecioLeido.keys())
#     PrecioLeidoValues = list(PrecioLeido.values())  
#     for LineaCamion in CamionLeido: #------------------Es una lista con diccionarios dentro        
#         for indice , Linea in enumerate(PrecioLeidoKeys):#--------Es un diccionario enorme
#             if Linea == LineaCamion["nombre"]:
#                 TotalCostos= TotalCostos + float(LineaCamion["cajones"]) * float(PrecioLeidoValues[indice])
#                 Total= Total + float(LineaCamion["cajones"]) * float(LineaCamion["precio"])
#     print("\n")
#     print(f"Total de costos vendidos en el lugar es : {TotalCostos:^10.2f}")
#     print("\n")
#     print(f"Hubo una ganancia de: {(TotalCostos - Total):^10.2f}")
#     print("\n")
#     return PrecioLeidoKeys, PrecioLeidoValues 

## Hacer informes. --------------------------------------------------------------------------------------------
# def hacer_informe(CamionLeido, PrecioLeidoKeys, PrecioLeidoValues):
# # Esta funcion recibe el camion leido como una lista de diccionarios y 2 listas mas que representan
# # la lista completa de precios de venta, separadas con frutas y precios.
#     Nombres = []
#     Cajones = []
#     Precios = []
#     Cambios = []
#     informe = ()
#     for Linea in CamionLeido:
#         Nombres.append(Linea['nombre'])
#         Cajones.append((int(Linea['cajones'])))
#         Precios.append(float(Linea['precio']))
#         for i , key in enumerate(PrecioLeidoKeys):
#             if key == Linea['nombre']:
#                 Cambios.append(round((float(PrecioLeidoValues[i]) - float(Linea['precio'])) , 2))
#                 break
#             informe = tuple(zip(Nombres , Cajones , Precios , Cambios))
#     return informe

## Funcion: Lectura completa de los arboles. ------------------------------------------------------------------
# def imprimir_informe(informe):
# # Esta funcion imprime una tabla de informe de costos de frutas como asi tambien cajones que se vendieron
# # y las ganancias.
#     Headers = ("Nombre" , "Cajones" , "Precios" , "Cambio")
#     ListaHeaders = list(Headers)
#     print(f"{ListaHeaders[0]:>10s} {ListaHeaders[1]:>10s} {ListaHeaders[2]:>10s} {ListaHeaders[3]:>10s}")
#     print(f"-----------------------------------------------")
#     for tupla in informe:
#         print(f"{tupla[0]:>10s} {tupla[1]:>10d} {tupla[2]:>10.2f} {tupla[3]:>10.2f}")
#     return None

# def informe_camion(camion , precios):
# # Funcion que corre en programa entero
#     CamionLeido = leer_camion(camion)
#     #CamionLeido = fileparse.parse_csv('C:\Python/Unsam Python/Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float] , has_headers = True)
#     print("\n")
    
#     PrecioLeido = leer_precios(precios)
#     #PrecioLeido = fileparse.parse_csv('C:\Python/Unsam Python/Data/precios.csv', types=[str,float], has_headers=False)
#     print("\n")
    
#     PrecioLeidoKeys, PrecioLeidoValues  = calculo_de_costos(CamionLeido , PrecioLeido)
#     informe = hacer_informe(CamionLeido, PrecioLeidoKeys, PrecioLeidoValues)
#     imprimir_informe(informe)
#     return None

# Main  --------------------------------------------------------------------------------------------------------
# informe_camion("camion" , "precios")







"""------------------------------------------------------------------------------------------------------------
Modificacion del archivo informe_funciones.
Ing.Lucas F. Quiroga H. Fecha: 19/04/2021. 
------------------------------------------------------------------------------------------------------------"""
# Import
import fileparse

# Funciones ---------------------------------------------------------------------------------------------------
## Funcion: Leer camion. --------------------------------------------------------------------------------------
def leer_camion(archivo):
# Lee un archivo csv con el contenido de un camion.
    import csv
    Total = 0
    camion =[]
    Nombre ="C:\Python/Unsam Python/Data/" + archivo + ".csv"
    camion = fileparse.parse_csv(Nombre , select = ['nombre', 'cajones', 'precio'], types = [str, int, float] , has_headers = True)
    Total = sum(float(Linea["cajones"]) * (Linea["precio"]) for Linea in camion)
    print()
    print(f"El costo del camion es: {Total:^10.2f}")
    return (camion)

## Funcion: Leer precios. -------------------------------------------------------------------------------------
def leer_precios(archivo):
# Lee los precios a partir de un archivo csv de precios
    import csv
    from pprint import pprint
    Precios = {}
    Nombre ="C:\Python/Unsam Python/Data/" + archivo + ".csv"
    Precios = fileparse.parse_csv(Nombre , types=[str,float], has_headers=False)
    return(Precios)

## Funcion: Calculo de costos. --------------------------------------------------------------------------------
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

# Main  --------------------------------------------------------------------------------------------------------
informe_camion("camion" , "precios")