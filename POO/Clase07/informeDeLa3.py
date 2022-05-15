"""------------------------------------------------------------------------------------------------------------
Informe para clase 7
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%
import sys
sys.argv # ['informe.py, 'camion.csv', 'precios.csv']
# Funciones  --------------------------------------------------------------------------------------------------
## FUNCIONES LEER CAMION --------------------------------------------------------------------------------------
# %%
# Lee el archivo camion
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
    Nombre ="C:\Python/Unsam Python/Data/" + archivo + ".csv"# <---------- Profesor: Considere un cambio de ruta para correr el script en su pc
    try:
        with open(Nombre , "r" , encoding="utf8") as Creacion:
            Lectura = csv.reader(Creacion)
            cabecera = next(Lectura)
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

## FUNCIONES FUNCION LEER PRECIOS -----------------------------------------------------------------------------
# %%
def leer_precios(archivo):
# Lee el archivo precios
    import csv
    from pprint import pprint
    OtroDicionario ={}
    Precios = {}
    Cabecera = []
    Nombre = "C:\Python/Unsam Python/Data/" + archivo + ".csv"
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

## FUNCIONES CALCULO DE COSTOS -------------------------------------------------------------------------------
# %%
def calculo_de_costos(CamionLeido , PrecioLeido):
# Realiza el calculo de los costos
    TotalCostos = 0
    PrecioLeidoKeys = list(PrecioLeido.keys())
    PrecioLeidoValues = list(PrecioLeido.values())
    for LineaCamion in CamionLeido: #------------------Es una lista con diccionarios dentro
        for indice , Linea in enumerate(PrecioLeidoKeys):#--------Es un diccionario enorme
            if Linea == LineaCamion["nombre"]:
                TotalCostos= TotalCostos + float(LineaCamion["cajones"]) * float(PrecioLeidoValues[indice])
    print(f"Total de costos vendidos en el lugar es : {TotalCostos}")
    print(f"Hubo una ganancia de: {round((TotalCostos - Total), 2)}")

## FUNCIONES FUNCION PRINCIPAL MAIN ---------------------------------------------------------------------------
def main(parametros):
# El main como programa principal
    archivo1 = ""
    archivo2 = ""
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
        archivo1 = sys.argv[1]
        archivo2 = sys.arg[2]
    else:
        archivo1 = "camion"
        archivo2 = "precios"
    CamionLeido = leer_camion(archivo1)
    print("\n")
    PrecioLeido = leer_precios(archivo2)
    print("\n")
    calculo_de_costos(CamionLeido , PrecioLeido )

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main(sys.argv)