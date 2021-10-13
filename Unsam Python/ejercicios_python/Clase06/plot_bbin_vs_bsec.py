"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 21/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%
import random
import matplotlib.pyplot as plt
import numpy as np

# Funciones ---------------------------------------------------------------------------------------------------
## FUNCIONES GENERAR LISTA ------------------------------------------------------------------------------------
# %%
def generar_lista(n, m):
# Devuelve una lista ordenada de n elementos diferentes entre 0 y m-1
    l = random.sample(range(m), k = n)
    l.sort()
    return l

## FUNCIONES FUNCION GENERAR ELEMENTO -------------------------------------------------------------------------
# %%
def generar_elemento(m):
# Devuelve un elemento aleatorio en el mismo rango de valores.
    return random.randint(0, m-1)

## FUNCIONES FUNCION BUSQUEDA SECUENCIAL ----------------------------------------------------------------------
# %%
def busqueda_secuencial_(lista, x):
# Si x está en la lista devuelve el índice de su primera aparición,
# de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
# que hace la función.
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps
## FUNCIONES FUNCION BUSQUEDA SECUENCIAL PROMEDIO -------------------------------------------------------------
# %%
def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom

## FUNCIONES FUNCION BUSQUEDA BINARIA --------------------------------------------------------------------------
# %%
def busqueda_binaria_(lista, x, verbose = False):
    # Búsqueda binaria
    # Precondición: la lista está ordenada
    # Devuelve -1 si x no está en lista;
    # Devuelve p tal que lista[p] == x, si x está en lista
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    Contador = 0
    while izq <= der:
        Contador += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos , Contador

## FUNCIONES FUNCION EXPERIMENTO BINARIO PROMEDIO --------------------------------------------------------------
# %%
def experimento_binario_promedio(lista, m, k):
    compb_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        compb_tot += busqueda_binaria_(lista,x)[1]
    compb_prom = compb_tot / k
    return compb_prom


# Main  --------------------------------------------------------------------------------------------------------
# %%
m = 10000
n = 100
lista = generar_lista(n, m)
# %%
# acá comienza el experimento
x = generar_elemento(m)
comps = busqueda_secuencial_(lista, x)[1]

# %%
m = 10000
k = 1000

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
plt.show()

# %%
# acá comienza el experimento
x = generar_elemento(m)
comps = busqueda_binaria_(lista, x)[1]

# %%
m = 10000
k = 1000

largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n, m) # genero lista de largo n
    comps_promedio[i] = experimento_binario_promedio(lista, m, k)

# ahora grafico largos de listas contra operaciones promedio de búsqueda.
plt.plot(largos,comps_promedio,label = 'Búsqueda binario')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
plt.show()

# A medida que crece el largo de la lista la complejidad de una busqueda binaria se hace mas benebola.