#--------------------------------------------------------------------
# %%
#
import timeit
import numpy as np
import random
import matplotlib.pyplot as plt
def ord_seleccion(lista):
# Ordena una lista de elementos según el método de selección.
# Pre: los elementos de la lista deben ser comparables.
# Post: la lista está ordenada.
    # posición final del segmento a tratar
    n = len(lista) - 1
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # reducir el segmento en 1
        n = n - 1
    return None
def buscar_max(lista, a, b):
# Devuelve la posición del máximo elemento en un segmento de
# lista de elementos comparables.
# La lista no debe ser vacía.
# a y b son las posiciones inicial y final del segmento
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max
def ord_insercion(lista):
# Ordena una lista de elementos según el método de inserción.
# Pre: los elementos de la lista deben ser comparables.
# Post: la lista está ordenada.
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
    return None
def reubicar(lista, p):
# Reubica al elemento que está en la posición p de la lista
# dentro del segmento [0:p-1].
# Pre: p tiene que ser una posicion válida de lista
    v = lista[p]
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v
    return None
def ord_burbujeo(lista):
# Ordena una lista de elementos según el método de La burbuja.
# Pre: los elementos de la lista deben ser comparables.
# Post: la lista está ordenada.
    for NumeroDePasada in range(len(lista) - 1 , 0 , -1):
        for i in range(NumeroDePasada):
            if lista[i] > lista[i + 1]:
                lista[i] , lista[i + 1] = lista[i + 1] , lista[i]
    return None
def generar_listas(Nmax):
#Contrato: Funcion generadora de listas de N elementos entre 1 y 1000
# Precondicion: Parametro N entero
# Poscondicion: Lista de tamaño N con valores entre 1 y 1000
    Lista = []
    for i in range (Nmax):
        Lista.append(random.randint(1 , 1000))
    return Lista
def experimento_timeit_seleccion(listas, num , metodo):
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
        tiempo_seleccion = timeit.timeit(metodo, number = num, globals = globals())
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    return tiempos_seleccion
#--------------------------------------------------------------------
# %%
#
listas = []
for N in range(1, 256):
    listas.append(generar_listas(N))
#----------------------------------------------------------------------------------------------------
tiempos_seleccion_seleccion = experimento_timeit_seleccion(listas, 100 , 'ord_seleccion(lista.copy())')
plt.plot(tiempos_seleccion_seleccion , color = "blue", linewidth = 2.5, label = "Seleccion")
#----------------------------------------------------------------------------------------------------
tiempos_seleccion_insercion = experimento_timeit_seleccion(listas, 100 , 'ord_insercion(lista.copy())')
plt.plot(tiempos_seleccion_insercion , color = "green", linewidth = 2.5, label = "Insecion")
#----------------------------------------------------------------------------------------------------
tiempos_seleccion_burbujeo = experimento_timeit_seleccion(listas, 100 , 'ord_burbujeo(lista.copy())')
plt.plot(tiempos_seleccion_burbujeo , color = "red", linewidth = 2.5, label = "burbujeo")
plt.legend(loc = 'upper left')