"""------------------------------------------------------------------------------------------------------------
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# %%
# Seccion 10.2
x = [1 , 2 , 3]
it = x.__iter__()
#--------------------------------------------------------------------
# %%
# Iteracion comun
it.__next__()
#--------------------------------------------------------------------
# %%
#
class Camion:
    def __init__(self):
        self.lotes = []

    def __iter__(self):
        return self.lotes.__iter__()

#--------------------------------------------------------------------
# %%
#
def regresiva(n):
    while n > 0:
        yield n
        n -= 1
#--------------------------------------------------------------------
# %%
#
for x in regresiva(10):
    print(x, end=' ')
# %%
x = regresiva(10)
#--------------------------------------------------------------------
# %%
#
x
# %%
x.__next__()
# %%