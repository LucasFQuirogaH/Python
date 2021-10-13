#--------------------------------------------------------------------
# %%
#
def sumar(lista):
# Devuelve la suma de los elementos en la lista.
    res = 0
    if len(lista) != 0:
        res = lista[0] + sumar(lista[1:])
    return res

#--------------------------------------------------------------------
# %%
#
sumar([1 , 2 , 3 , 4 , 5])

#--------------------------------------------------------------------
# %%
#
def sumar(lista, suma = 0):
# Devuelve la suma de los elementos en la lista.
    res = suma
    if len(lista) != 0:
        res = sumar(lista[1:], lista[0] + suma)
    return res
#--------------------------------------------------------------------
# %%
#
sumar ([1 , 2 , 3 , 4 , 5])
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
#
def promediar(lista):
    if len(lista) == 1:
        res = lista[0]
    else:
        res = promediar(lista[1:]) ???
    return res
#--------------------------------------------------------------------
# %%
#
def promediar_aux(lista):
    suma = lista[0]
    cantidad = 1
    if len(lista) > 1:
        suma_resto, cantidad_resto = promediar_aux(lista[1:])
        suma += suma_resto
        cantidad += cantidad_resto
    return suma, cantidad
#--------------------------------------------------------------------
# %%
#
def promediar(lista):
# Devuelve el promedio de los elementos de una lista de números."""
    #--------------------------------------------------------------------
    def promediar_aux(lista):
        suma = lista[0]
        cantidad = 1
        if len(lista) > 1:
            suma_resto, cantidad_resto = promediar_aux(lista[1:])
            suma += suma_resto
            cantidad += cantidad_resto
        return suma, cantidad
    #--------------------------------------------------------------------
    suma, cantidad = promediar_aux(lista)
    return suma / cantidad
