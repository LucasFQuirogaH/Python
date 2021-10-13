def sumar_enteros(desde, hasta):
# Calcula la sumatoria de los números entre desde y hasta.
# Si hasta < desde, entonces devuelve cero.
# Pre: desde y hasta son números enteros
# Pos: Se devuelve el valor de sumar todos los números del intervalo
# [desde, hasta]. Si el intervalo es vacío se devuelve 0
    Suma = 0
    if desde >= hasta:
        return 0
    else:
        while (desde != hasta):
            Suma += desde
            desde +=1
        return Suma
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
#
def recursivo (n):
    if n == 1:
        return n
    else:
        res = n + recursivo(n - 1)
    return res
#--------------------------------------------------------------------
# %%
#
recursivo(100)
# %%
