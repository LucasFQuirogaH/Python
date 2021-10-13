"""------------------------------------------------------------------------------------------------------------
time Ordenamiento.
Ing.Lucas F. Quiroga H. Fecha: 09/06/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import ------------------------------------------------------------------------------------------------------
# %%
import timeit
import numpy as np
import random
import matplotlib.pyplot as plt
# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Ordenar por seleccion ---------------------------------------------------------------------------
# %%
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
        print("DEBUG: ", p, n, lista)
        # reducir el segmento en 1
        n = n - 1
    return None
## Funciones: Buscar Maximo -----------------------------------------------------------------------------------
# %%
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
## Funciones: Ordenar por insercion ---------------------------------------------------------------------------
# %%
def ord_insercion(lista):
# Ordena una lista de elementos según el método de inserción.
# Pre: los elementos de la lista deben ser comparables.
# Post: la lista está ordenada.
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
        print("DEBUG: ", lista)
    return None
## Funciones: Funcion reubicar --------------------------------------------------------------------------------
# %%
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
## Funciones: Busqueda con el metodode la burbuja -------------------------------------------------------------
# %%
def ord_burbujeo(lista):
# Ordena una lista de elementos según el método de La burbuja.
# Pre: los elementos de la lista deben ser comparables.
# Post: la lista está ordenada.
    for NumeroDePasada in range(len(lista) - 1 , 0 , -1):
        for i in range(NumeroDePasada):
            if lista[i] > lista[i + 1]:
                lista[i] , lista[i + 1] = lista[i + 1] , lista[i]
                print("DEBUG: ", lista)
    return None
## Funciones: Generar Listas ----------------------------------------------------------------------------------
# %%
def generar_listas(Nmax):
#Contrato: Funcion generadora de listas de N elementos entre 1 y 1000
# Precondicion: Parametro N entero
# Poscondicion: Lista de tamaño N con valores entre 1 y 1000
    Lista = []
    for i in range (Nmax):
        Lista.append(random.randint(1 , 1000))
    return Lista
## Funciones: Experimento timeit seleccion --------------------------------------------------------------------
# %%
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
        tiempo_seleccion = timeit.timeit('ord_insercion(lista.copy())', number = num, globals = globals())
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    return tiempos_seleccion
## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    listas = []
    for N in range(1, 256):
        listas.append(generar_listas(N))
    tiempos_seleccion = experimento_timeit_seleccion(listas, 4)
    plt.plot(tiempos_seleccion)
    return None
# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()
# %%

"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
"""
plt.show()
X = np.linspace(-(np.pi), (np.pi), 256)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C)
plt.plot(X, S)
plt.plot(X, C, color="blue", linewidth=2.5, linestyle = "-", label = "coseno")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle = "-", label = "seno")
plt.legend(loc='upper left')
plt.grid()
plt.ylabel("Seno y Coseno")
plt.xlabel("angulo")
plt.title("Grafico Posta")
ax = plt.gca()  # gca es 'get current axis' ó 'tomar eje actual'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
plt.annotate(r'cos(rac{2i}{3})=-rac{1}{2}$',
            xy=(t, np.cos(t)), xycoords='data',
            xytext=(-90, -50), textcoords='offset points', fontsize=16,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.plot([t, t],[0, np.sin(t)], color='red', linewidth=2.5, linestyle = "--")
plt.scatter([t, ],[np.sin(t), ], 50, color='red')
plt.annotate(r'sin(rac{2i}{3})=rac{qrt{3}}{2}$',
            xy=(t, np.sin(t)), xycoords='data',
            xytext=(+10, +30), textcoords='offset points', fontsize=16,
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
for label in ax.get_xticklabels() + ax.get_yticklabels():
label.set_fontsize(16)
label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
plt.show()
"""