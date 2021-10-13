# Funciones  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def leer_camion(archivo):
    import csv
    from pprint import pprint
    global Total
    Total = 0
    UnDiccionario = {}
    cabecera =""
    camion =[]
    Nombre ="C:\Python/Unsam Python/Data/" + archivo + ".csv"#<--------------------------------------- Profesor: Considere un cambio de ruta para correr el script en su pc
    try:
        with open(Nombre , "r" , encoding="utf8") as Creacion:
            Lectura = csv.reader(Creacion)
            cabecera = next(Lectura)
            for Linea in Lectura:
                UnDiccionario = dict(zip(cabecera, Linea))
                Total = Total + (float(UnDiccionario["cajones"]) * float(UnDiccionario["precio"]))
                camion.append(UnDiccionario)
                UnDiccionario = {}
        print(f"El costo del camion es: {Total:^10.2f}")
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
    Nombre ="C:\Python/Unsam Python/Data/" + archivo + ".csv"
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
    TotalCostos = 0.0
    PrecioLeidoKeys = list(PrecioLeido.keys())
    PrecioLeidoValues = list(PrecioLeido.values())
#---------------------------------------------------------------------------------------------------------------    
    for LineaCamion in CamionLeido: #------------------Es una lista con diccionarios dentro        
        for indice , Linea in enumerate(PrecioLeidoKeys):#--------Es un diccionario enorme
            if Linea == LineaCamion["nombre"]:
                TotalCostos= TotalCostos + float(LineaCamion["cajones"]) * float(PrecioLeidoValues[indice])
    print("\n")
    print(f"Total de costos vendidos en el lugar es : {TotalCostos:^10.2f}")
    print("\n")
    print(f"Hubo una ganancia de: {(TotalCostos - Total):^10.2f}")
    print("\n")
    """-----------------------------------------------------------------------------------------------------------
    Realice una funcion hacer informe que es llamada por la funcion costo de calculos, primitiva del punto 
    -----------------------------------------------------------------------------------------------------------"""
    hacer_informe(CamionLeido, PrecioLeidoKeys, PrecioLeidoValues) 
    
    
def hacer_informe(CamionLeido, PrecioLeidoKeys, PrecioLeidoValues):
    Headers = ("Nombre" , "Cajones" , "Precios" , "Cambio")
    ListaHeaders = list(Headers)
    Rayas = "-------"
    print(f"{ListaHeaders[0]:>10s} {ListaHeaders[1]:>10s} {ListaHeaders[2]:>10s} {ListaHeaders[3]:>10s}")
    print(f"{Rayas:>10s} {Rayas:>10s} {Rayas:>10s} {Rayas:>10s}")
    for LineaCamion in CamionLeido: #------------------Es una lista con diccionarios dentro        
        for indice , Linea in enumerate(PrecioLeidoKeys):#--------Es un diccionario enorme
            if Linea == LineaCamion["nombre"]:
                PrecioEnElLugar =  PrecioLeidoValues[indice]
                ElPrecioEnElLugar = "$" + str(PrecioEnElLugar)
                Cambio = '%0.2f' % ((float(PrecioLeidoValues[indice])) - (float(LineaCamion['precio'])))
                ElCambio = "$" + str(Cambio)
                print(f"{Linea:>10s} {(LineaCamion['cajones']):>10s} {ElPrecioEnElLugar:>10s} {(ElCambio):>10s}")

# Main  --------------------------------------------------------------------------------------------------------
CamionLeido = leer_camion("camion")
print("\n")
PrecioLeido = leer_precios("precios")
print("\n")
calculo_de_costos(CamionLeido , PrecioLeido )