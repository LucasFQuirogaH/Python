"""--------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 5.24: Histograma de altos de Jacarandás
Usando tu trabajo en el Ejercicio 4.16, generá un histograma con las alturas de los Jacarandás en el dataset.
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
import os
import matplotlib.pyplot as plt
import numpy as np
import pprint

# os.path.join('Data', 'arbolado-en-espacios-verdes.csv')
# arboleda = leer_arboles("arbolado-en-espacios-verdes")

# altos = [arbol["altura_tot"] for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
# print("Hola")
# plt.hist(altos,bins = 25)
# plt.show()


# 5.25

# os.path.join('Data', 'arbolado-en-espacios-verdes.csv')
# arboleda = leer_arboles("arbolado-en-espacios-verdes")

# altos = [arbol["altura_tot"] for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
# diametros = [arbol["diametro"] for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]

# plt.scatter(diametros,altos)
# plt.show()

# Convertí la lista generada en un ndarray de numpy, de esa forma podés usar rebanadas para obtener
# un vector d con diámteros y otro h con alturas inmediatamente.

os.path.join('Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles("arbolado-en-espacios-verdes")
Jacarandas = [arbol for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
bandera = 1
for arbol in Jacarandas:
    a = np.array(list(arbol.values()))
    if bandera == 0:
        Arreglo = np.array((Arreglo , a))
    else:
        Arreglo = a
        bandera = 0

print(Arreglo.shape)

# plt.scatter(Arreglo[0:N,4],Arreglo[0:N , 3])
# plt.show()