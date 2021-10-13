"""------------------------------------------------------------------------------------------------------------
M E T O D O  M E R G E
Ing.Lucas F. Quiroga H. Fecha: 11/06/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
# F u n c i o n   M e r g e  ----------------------------------------
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
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R   P A R A   P R O B A R  --------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
#
lista = [9 , 5 , 4 , 3 , 8 , 7 , 1 , 3 , 6 , 2 , 0]
merge_sort(lista)