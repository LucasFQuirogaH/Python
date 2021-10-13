"""------------------------------------------------------------------------------------------------------------
Busquedas Binaria y Secuencial
Ing.Lucas F. Quiroga H. Fecha: 22/06/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
## Funciones: Busqueda Secuencial -----------------------------------------------------------------------------
# %%
def BusquedaSecuencial(lista, x):
# Si x está en la lista devuelve el índice de su primera aparición, de lo contrario devuelve -1.
# Además devuelve la cantidad de comparaciones que hace la función.
# Pre: Una lista y el valor
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i , z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps
## Funciones: Busqueda Binaria --------------------------------------------------------------------------------
# %%
def BusquedaBinaria(lista, x):
# Búsqueda binaria
# Precondición: la lista está ordenada
# Devuelve -1 si x no está en lista;
# Devuelve p tal que lista[p] == x, si x está en lista
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    Contador = 0
    while izq <= der:
        Contador += 1
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio    # elemento encontrado!
            break
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos , Contador