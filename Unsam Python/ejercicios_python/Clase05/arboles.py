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

os.path.join('Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles("arbolado-en-espacios-verdes")

# 5.24
altos = [arbol["altura_tot"] for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
print("Hola")
plt.hist(altos,bins = 25)
plt.show()


# 5.25
"""Ejercicio 5.25: Scatterplot (diámetro vs alto) de Jacarandás
En este ejercicio introducimos un nuevo tipo de gráfico: el gráfico de dispersión o scatterplot. El mismo usa coordenadas cartesianas para mostrar
los valores de dos variables para un conjunto de datos.
En este caso vamos a graficar un punto en el plano (x,y) por cada árbol en el dataset (o para cada arbol de cierta especie). El punto
correspondiente a un árbol con diámetro d y altura h será ubicado en la posición x=d y y=h. Este tipo de gráfico permite visualizar relaciones o
tendencias entre las variables y es muy útil en el análisis exploratorio de datos.
Usando como base tu trabajo del Ejercicio 4.17, vas a generar un scatterplot para visualizar la relación entre diámetro y alto de los Jacarandás
del dataset.
Si ya tenés una lista o un vector d con diámetros y otra h con altos, es sencillo hacer un primer scatterplot:
import matplotlib.pyplot as plt
plt.scatter(d,h)"""


""" Correccion del profesor.
Hola Lucas Quiroga,
(mail enviado automáticamente con Python)
Esta semana te tocó a vos que te corrijan de la Unidad 5: 5.25.
La consigna del ejercicio: Consigna
Tu archivo evaluado: arboles.py
Obtuviste la siguiente corrección por parte del plantel docente:
hola, el codigo esta bien pero los 2 graficos son scatter y se pedian histogramas
Tu código fue revisado por José Crespo. Cualquier duda o consulta sobre la corrección escribile un mensaje vía Slack
(http://python-unsam-2021c1.slack.com/team/U01PGV0MSBA).

Saludos.
UNSAM Python"""

# En la correccion del ejercicio me piden que realice un Histograma, pero el enunciado me dice hacer un scatter.

os.path.join('Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles("arbolado-en-espacios-verdes")

altos = [arbol["altura_tot"] for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]
diametros = [arbol["diametro"] for arbol in arboleda if arbol["nombre_com"] == "Jacarandá"]

plt.scatter(diametros,altos)
plt.show()

# 5.26

# os.path.join('Data', 'arbolado-en-espacios-verdes.csv')
# arboleda = leer_arboles("arbolado-en-espacios-verdes")
# especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
# medidas = medidas_de_especies(especies, arboleda)

# plt.scatter(diametros,altos)
# plt.show()

