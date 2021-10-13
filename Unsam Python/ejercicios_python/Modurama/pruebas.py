#--------------------------------------------------------------------
# %%
#
import busquedas
buscado = 15
lista = [2 , 3 , 5 , 7 , 11 , 13 , 15]
#--------------------------------------------------------------------
# %%
# Secuencial
Posicion , Comparaciones = busquedas.BusquedaSecuencial(lista , buscado)
print(f'Posicion:  {Posicion}')
print(f'Comparaciones: {Comparaciones}')
# %%
# Binario
Posicion , Comparaciones = busquedas.BusquedaBinaria(lista , buscado)
print(f'Posicion:  {Posicion}')
print(f'Comparaciones: {Comparaciones}')
# %%
