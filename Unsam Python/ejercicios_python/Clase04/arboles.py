"""--------------------------------------------------------------------------------------------------------------------------------------------------
BUENO NADA . .  VAMOS!
--------------------------------------------------------------------------------------------------------------------------------------------------"""
# FUNCIONES -----------------------------------------------------------------------------------------------------------------------------------------
## Funcion 1: Lectura completa de los arboles. ------------------------------------------------------------------------------------------------------
def leer_arboles(nombre_archivo):
    import csv
    Nombre ="Data/" + nombre_archivo + ".csv"
    try:
        with open(Nombre , "r" , encoding="utf8") as Creacion:
            Lectura = csv.reader(Creacion)
            Cabecera = next(Lectura)
            LineaActual = next(Lectura)
            Tipos = [type(elemento) for elemento in LineaActual]
            ListaFinal = [{Nombre: Funcion(Valor) for Nombre , Funcion , Valor in zip(Cabecera , Tipos , LineaActual)} for LineaActual in Lectura]
    except ValueError:
        print("Existe un problema con el archivo selecionado")
    except FileNotFoundError:
        print("El archivo no se encuentra en el directorio")
    except IndexError:
        print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
    return (ListaFinal)
## Funcion 2: Diccionario con especies especificas y devolucion de alturas y diametros. -------------------------------------------------------------
def medidas_de_especies(especies , Arboleda):
    ListaParEspecieDiametro =[[(arbol["altura_tot"] , arbol["diametro"]) for arbol in Arboleda if arbol["nombre_com"] == UnaLinea] for UnaLinea in especies]
    ElDiccionario = dict(zip(especies , ListaParEspecieDiametro))
    return ElDiccionario
# MAIN ----------------------------------------------------------------------------------------------------------------------------------------------
# 4.18
import pprint
ListaAlturaJacarandá = []
Arboleda = leer_arboles("arbolado-en-espacios-verdes")
# pprint.pprint(Arboleda)

# 4.19
ListaAlturaJacarandá = [arbol["altura_tot"] for arbol in Arboleda if arbol["nombre_com"] == "Jacarandá"]
# pprint.pprint(ListaAlturaJacarandá)

# 4.20
ListaAlturaDiametroJacarandá = [(arbol["altura_tot"] , arbol["diametro"]) for arbol in Arboleda if arbol["nombre_com"] == "Jacarandá"]
# pprint.pprint(ListaAlturaDiametroJacarandá)

# 4.21
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
ElDiccionario = medidas_de_especies(especies , Arboleda)
# pprint.pprint(ElDiccionario)