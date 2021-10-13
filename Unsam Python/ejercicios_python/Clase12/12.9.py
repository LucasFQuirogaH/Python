"""------------------------------------------------------------------------------------------------------------
12.9 Escribí una función merge3sort que funcione igual que el merge sort pero en lugar de dividir la lista de
entrada en dos partes, la divida en tres partes. Deberás escribir la función merge3sort(lista1, lista2, lista3).
Ing.Lucas F. Quiroga H. Fecha: 11/06/2021 Retroceder nunca, rendirse jamas.
------------------------------------------------------------------------------------------------------------"""
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def merge3sort(lista1, lista2, lista3):
#Contrato:
# Precondicion:
# Poscondicion:
    return None
#--------------------------------------------------------------------------------------------------------------
import random
def merge_sort(lista):
# Ordena lista mediante el método merge sort. Divide en 2 hasta que
# quedan todos de uno.Luego emppeza a armar de a dos, luegode a
# cuatro. Luego de  ocho y asi. Despues en la medida que va
# comparando, siempre compara los primeros valores de cada tanda.
# Siempre compara de dos.
# Pre: lista debe contener elementos comparables.
# Devuelve: una nueva lista ordenada.
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva
#--------------------------------------------------------------------
def merge(lista1, lista2):
# Intercala los elementos de lista1 y lista2 de forma ordenada.
# Pre: lista1 y lista2 deben estar ordenadas.
# Devuelve: una lista con los elementos de lista1 y lista2.
    i , j = 0 , 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1
    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado