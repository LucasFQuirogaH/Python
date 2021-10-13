#--------------------------------------------------------------------
# %%
#
mi_var = {'cero' : 0 , 'uno' : 1}
print(mi_var[0])
# %%
import numpy as np
a = np.array([[1, 2 , 3 , 4] , [5 , 6 , 7 , 8] , [9 , 10 , 11 , 12] , [13 , 14 , 15 , 16]])
b = a[1:3]
# %%
b
# %%
d = {}
dias = ['lunes' , 'martes' , 'miercoles' , 'jueves' , 'viernes' , 'sabado' , 'domingo']
dias_abreviados = ['lu' , 'ma' , 'mi' , 'ju' , 'vi' , 'sa' , 'do']
while len(d) < 6:
    dia = dias[len(d)]
    abr = dias_abreviados[len(d)]
    d[dia] = abr
print (d['sabado'])
# %%
a = ['n' , 'e' , 'p']
b = ['R' , 43 , 78]
d = dict(zip(a,b))
if (d['e'])%2 == 0:
    print('par')
else:
    print('Impar')
# %%
lista = [2 , 4 , 6 , 8 , 10]
{x: x**2 for x in range (10) if x in lista}
# %%
def funct(a, b):
    c = a + b
c = 3
c = funct(2 , 3)
#--------------------------------------------------------------------
# %%
#
r = [x * y for x in range (-10 , 10) if x > 0 and x%2  == 1 for y in [1 , 0 , -1] if y != 0]
# %%
r
# %%
lista = ['uno' , 'dos' , 'tres']
print (lista[1])
# %%
for i , c in enumerate('pavada'):
    if i != (i//2) * 2:
        print(c , end = '')
# %%
n = 5
lista = [1] * n
for i in range(1 , n):
    lista [i] = lista [i - 1] + lista [i] + lista [i + 1]
# %%
def una_funcion():
    if 'a' or 'e' in casa:
        return True
    else:
        return False
#--------------------------------------------------------------------
# %%
#
una_funcion()
# %%
suma = 0
n = 5
for i in range(n):
    for j in range(n):
        if mat[i][j] == 0:
            suma += 1
#--------------------------------------------------------------------
# %%
#
suma = n * n - suma
#--------------------------------------------------------------------
# %%
#
n = 5
lista = [1] * n
for i in range(n):
    if i + 1 < n and lista[i + 1] == 1:
        lista[i] += lista[i + 1]
lista[4] = 2
#--------------------------------------------------------------------
# %%
#
lista
# %%
lista = [1 , 2 , 3]
n = 2
for k in range(10):
    try:
        if k < n and lista[k] == 3:
            print('caso 1')
    except Exception:
        print('caso 2')
# %%
a = [1]
b = [2 , 3]
c = [4 , 5 , 6]
k = [a , b , c]
m = k.copy()
m[1].append(7)
print(k)
# %%
id(m[1]) == id(k[1])
# %%
frutas = "Manzana , Naranja , Mandarina"
frutas[0] = 'm'
# %%
def func(a):
    a += 1
a = 1
a = func(a)
a = a + 1
#--------------------------------------------------------------------
# %%
cos(4)
# %%
from math import sqrt as cos
cos(4)
# %%
sin(0.5)
# %%
i = 0
suma = 0
while i <= 10:
    suma += i
#--------------------------------------------------------------------
# %%
#
print(suma)
# %%
