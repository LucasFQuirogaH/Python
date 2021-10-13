# %%
# Full
import timeit as tt
import time
import numpy as np
import random
import matplotlib.pyplot as plt
from busquedas import ord_seleccion
from busquedas import ord_insercion
# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Experimento timeit seleccion --------------------------------------------------------------------
def experimento_timeit_seleccion(listas, num):
# Realiza un experimento usando timeit para evaluar el método
# de selección para ordenamiento de listas
# con las listas pasadas como entrada
# y devuelve los tiempos de ejecución para cada lista
# en un vector.
# El parámetro 'listas' debe ser una lista de listas.
# El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método para cada lista.
    tiempos_seleccion = []
    global lista
    for lista in listas:
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ord_insercion(lista.copy())', number = num, globals = globals())
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    return tiempos_seleccion
## Funciones: Generar Lista -----------------------------------------------------------------------------------
def generar_lista(n):
#Contrato: Funcion generadora de listas de N elementos entre 1 y 1000
# Precondicion: Parametro N entero
# Poscondicion: Lista de tamaño N con valores entre 1 y 1000
    Lista = []
    for i in range (n):
        Lista.append(random.randint(1 , 1000))
    return Lista
listas = []
for N in range(1, 256):
    listas.append(generar_lista(N))
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
tiempos_seleccion = experimento_timeit_seleccion(listas, 10)
plt.plot(tiempos_seleccion)
# %%
