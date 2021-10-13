#--------------------------------------------------------------------
# %%
#
class Lote:
    def __init__(self, f ,c , p):
        self.nombre = f
        self.cajones = c
        self.precio = p

    def __repr__(self):
        return f'Lote({self.nombre},{self.cajones},{self.precio})'

    def __str__(self):
            return f'Lote: {repr(self.nombre)} / {self.cajones} / ${self.precio}'

    def costo(self):
        return self.precio * self.cajones

    def vender(self , n):
        self.cajones -= n

#--------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
#
milote = Lote('Naranja' , 100 , 32.2)
print(milote)
# %%
print(repr(milote))
# %%
milote = Lote('Naranja' , 100 , 32.2)
print(milote.cajones)
# %%
milote = Lote('Naranja' , 100 , 32.2)
print(milote.vender())
# %%
#--------------------------------------------------------------------
# %%
#
class Lote_inf(Lote):
    def costo(self):
        return 1.25 *self.cajones * self.precio
milote = Lote_inf("Pera" , 100 , 10)
print(milote.costo())
# %%
import datetime
a = datetime.date(2020 , 9 , 21)
b = datetime.date(2020 , 5 , 21)
x = a-b
print(type(x))
# %%
import os
os.mkdir('carpeta_mama')
#--------------------------------------------------------------------
# %%
#
os.mkdir('carpeta_mama/carpetahija')
#--------------------------------------------------------------------
# %%
#
import shutil
shutil.rmtree('carpeta_mama')
# %%
# %%
def suma_triang(n):
    return suma_triang(n-1) + n
#--------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
#
print(suma_triang(10))
# %%
def par(n):
    return impar (n - 1)
def impar(n):
    if n == 0:
        return False
    return par(n - 1)
#--------------------------------------------------------------------
impar (4)
# %%
a = [1 , 2 , 3 , 4 , 5]
b = (2 * x for x in a)
#--------------------------------------------------------------------
# %%
#
len(b)
# %%
class Jugador:
    def __init__(self , x , y):
        self.x = x
        self.y = y
        self.salud = 100

    def lastimar (self , golpe):
        self.salud -= golpe
#--------------------------------------------------------------------
# %%
#
juan = Jugador(12 , 10)
#--------------------------------------------------------------------
# %%
#
juan.lastimar(20)
# %%
print(juan)
# %%
juan.salud
# %%
def iterador (n):
    for i in range (n):
        if i // 2 == i / 2:
            yield i
#--------------------------------------------------------------------
# %%
#
pares = iterador(100)
print(pares)
# %%
print(os.getcwd())
# %%
os.getcwd

# %%
