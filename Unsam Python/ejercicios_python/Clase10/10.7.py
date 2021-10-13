#--------------------------------------------------------------------
# %%
# Funciones
import time
def cuadrados():
    n = 0
    while True:
        time.sleep(0.5)
        n += 1
        yield n * n
#--------------------------------------------------------------------
# Funcion Pares
def pares(nums):
    for c in nums:
        if c%2 == 0:
            yield c
#--------------------------------------------------------------------
def primeros (nums):
    for c in nums:
        if c < 100:
            yield c
        else:
            nums.close()
            yield c
            # return c
#--------------------------------------------------------------------
# %%
#
for elemento in cuadrados():
    print(elemento)
#--------------------------------------------------------------------
# %%
#
Cuadrados = cuadrados()
next(Cuadrados)
# %%
#
for elemento in pares(cuadrados()):
    print(elemento)
#--------------------------------------------------------------------
# %%
#
# while True:
#     print(primeros(cuadrados()))
# %%
#
for elemento in primeros(cuadrados()):
    print(elemento)
