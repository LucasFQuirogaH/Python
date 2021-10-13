"""------------------------------------------------------------------------------------------------------------
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
## Funciones: Busqueda de Maximo ------------------------------------------------------------------------------
# %%
def BusquedaLineal(Lista, Buscado):
Posicion = -1
for indice , elemento in enumerate(Lista):
    if elemento == Buscado:
        Posicion = indice
        break
return(Posicion)