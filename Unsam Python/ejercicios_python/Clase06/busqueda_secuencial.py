"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%



# Funciones ---------------------------------------------------------------------------------------------------
## FUNCIONES FUNCION BUSQUEDA LINEAL --------------------------------------------------------------------------
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
# Main  --------------------------------------------------------------------------------------------------------
# %%
Buscado = 11
Lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
# %%
# Posicion = busqueda_lineal_lordenada(Lista, Buscado)
# print(Posicion)
# %%
print(busqueda_secuencial_(Lista , Buscado)[1])
# %%
