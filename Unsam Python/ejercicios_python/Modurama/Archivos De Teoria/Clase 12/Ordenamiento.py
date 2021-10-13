"""------------------------------------------------------------------------------------------------------------
O R D E N A M I E N T O S
Ing.Lucas F. Quiroga H. Fecha: 11/06/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
# Metodos .-
# O r d e n a m i e n t o   p o r   s e l e c c i o n  -------------------------------------------------------
def ord_seleccion(lista):
# Ordena una lista de elementos según el método de selección. Busca el maximo, lo ubica al final y luego
# sigue con la busqueda en N - 1. Usa buscar Max como funcion auxiliar.
# Pre: Los elementos de la lista deben ser comparables.
# Post: La lista está ordenada.
    # posición final del segmento a tratar
    n = len(lista) - 1
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        print("DEBUG: ", lista)
        # reducir el segmento en 1
        n = n - 1
#--------------------------------------------------------------------
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
#--------------------------------------------------------------------------------------------------------------
# O r d e n a m i e n t o   p o r   i n s e c c i o n  --------------
def ord_insercion(lista):
# Ordena una lista de elementos según el método de inserción. Arranca con el segundo para compararse con el
# primero. Luego con el tercero para compararse con el primero y el segundo. Requiere de una funcion auxiliar
# llamada reubicar.
# Pre: los elementos de la lista deben ser comparables.
# Post: la lista está ordenada.
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
        print("DEBUG: ", lista)
    return None
#--------------------------------------------------------------------
def reubicar(lista, p):
# Reubica al elemento que está en la posición p de la lista
# dentro del segmento [0:p-1].
# Pre: p tiene que ser una posicion válida de lista.
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
#--------------------------------------------------------------------------------------------------------------
# O r d e n a m i e n t o   p o r   b u r b u j e o  ----------------
def ord_burbujeo(lista):
# Metodo de la burbuja. Se le asigna una lista y la devuelve ordenada.
# Pre: Los elementos de la lista deben ser comparables.
# Post: Lista ordenada.
    for NumeroDePasada in range(len(lista) - 1 , 0 , -1):
        for i in range(NumeroDePasada):
            if lista[i] > lista[i + 1]:
                lista[i] , lista[i + 1] = lista[i + 1] , lista[i]
                print("DEBUG: ", lista)
    return None
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R   P A R A   P R O B A R   L A S   F U N C I O N E S
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------------------------------------------------
lista = [6 , 5 , 3 , 1 , 8 , 7 , 2 , 4]
#--------------------------------------------------------------------
# %%
# Seleccion
ord_seleccion(lista)
#--------------------------------------------------------------------
# %%
# Insercion
ord_insercion(lista)
#--------------------------------------------------------------------
# %%
# Burbujeo
ord_burbujeo(lista)
# %%
