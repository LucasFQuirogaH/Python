#--------------------------------------------------------------------
# %%
#
import random
#--------------------------------------------------------------------
def merge_sort(lista):
# Ordena lista mediante el método merge sort.
# Pre: lista debe contener elementos comparables.
# Devuelve: una nueva lista ordenada
    contador = 0
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq , contador = merge_sort(lista[:medio])
        der , contador = merge_sort(lista[medio:])
        lista_nueva , contador = merge(izq, der)
    return lista_nueva , contador
#--------------------------------------------------------------------
def merge(lista1, lista2):
# Intercala los elementos de lista1 y lista2 de forma ordenada.
# Pre: lista1 y lista2 deben estar ordenadas.
# Devuelve: una lista con los elementos de lista1 y lista2
    i, j = 0, 0
    resultado = []
    contador = 0
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
        contador += 1
    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado , contador
#--------------------------------------------------------------------
# %%
#
Lista , Comparaciones = merge_sort([3, 1, 0, 4, 2])
print()
print(f"Lista ordenada: {Lista}")
print(f"Cantidad de comparaciones: {Comparaciones}")
# %%
