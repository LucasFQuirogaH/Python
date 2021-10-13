# Funciones  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def leer_camion(archivo):
    import csv
    from pprint import pprint
    global Total
    Total = 0
    UnDiccionario = {}
    cabecera =""
    camion =[]
    Mas100 = []
    NombreDeCajones = []
    NombreDeCajones2 = {}
    Stock = {}
    Nombre ="Data/" + archivo + ".csv"# <---------- Profesor: Considere un cambio de ruta para correr el script en su pc
    try:
        with open(Nombre , "r" , encoding="utf8") as Creacion:
            Lectura = csv.reader(Creacion)
            cabecera = next(Lectura)
 
            
            
            # camion.append((dict(zip(cabecera, Linea))) for Linea in Lectura)
            
            
            for Linea in Lectura:
                UnDiccionario = dict(zip(cabecera, Linea))
                Total = Total + (float(UnDiccionario["cajones"]) * float(UnDiccionario["precio"]))
                camion.append(UnDiccionario)
                UnDiccionario = {}
            
            
            
            
            
            Total2 = sum ([(float(OtraLinea["cajones"]))*(float(OtraLinea["precio"])) for OtraLinea in camion])
            print(Total2)
            
            
            Mas100 = [ OtraLinea for OtraLinea in camion if (int(OtraLinea["cajones"])) > 100 ]
            print("\n")
            pprint(Mas100)
            
            # 4.13
            NombreDeCajones = [(OtraLinea["nombre"] , OtraLinea["cajones"]) for OtraLinea in camion]
            print("\n")
            print(NombreDeCajones)
            
            NombreDeCajones2 = {(OtraLinea["nombre"] , OtraLinea["cajones"]) for OtraLinea in camion}
            print("\n")
            print(f"Otros cajones: {NombreDeCajones2}")
            
            Stock = {OtraLinea["nombre"]: 0 for OtraLinea in camion}
            print("\n")
            print(f"El stock es: {Stock}")
   
                
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