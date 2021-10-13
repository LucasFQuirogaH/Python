"""------------------------------------------------------------------------------------------------------------
Búsquedas.
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%



# Funciones ---------------------------------------------------------------------------------------------------
## FUNCIONES FUNCION 1 BUSQUEDA LINEAL LORDENADA --------------------------------------------------------------
# %%
def busqueda_lineal_lordenada(Lista, Buscado):
    Posicion = -1
    Lista.sort()
    for indice , elemento in enumerate(Lista):
        if elemento == Buscado:
            Posicion = indice
            break
        elif elemento > Buscado:
            Posicion = -1
            print()
            print("No se encontro")
            break
    return(Posicion)

# Main  --------------------------------------------------------------------------------------------------------
# %%
Buscado = 11
Lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
Posicion = busqueda_lineal_lordenada(Lista, Buscado)
print(Posicion)

# %%
