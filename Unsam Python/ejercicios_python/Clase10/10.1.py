"""------------------------------------------------------------------------------------------------------------
Ejercicio 10.1
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
# 10.1
a = [1, 9, 4, 25, 16]
#--------------------------------------------------------------------
# %%
#
i = a.__iter__()
# %%
i
# %%
i.__next__()
# %% Probando sobre un archivo
f = open('C:\Python/Unsam Python/Data/camion.csv')
#--------------------------------------------------------------------
# %%
# El iterador
f.__iter__()
# %%
# El next
next(f)
# %%
