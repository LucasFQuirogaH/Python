#--------------------------------------------------------------------
# %%
# Definicion de clase
class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.salud = 100
#--------------------------------------------------------------------
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
#--------------------------------------------------------------------
    def lastimar(self, pts):
        self.salud -= pts
#--------------------------------------------------------------------
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
# Lotes
import lote
a = lote.Lote('Pera', 100, 490.10)
b = lote.Lote("Manzana" , 50 , 122.34)
c = lote.Lote("Naranja" , 75 , 91.75)
#--------------------------------------------------------------------
# %%
#
lotes = [a, b, c]
#--------------------------------------------------------------------
# %%
#
for c in lotes:
    print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')
# %%
import fileparse
with open('C:\Python/Unsam Python/Data/camion.csv' , encoding = "utf8") as lineas: # Datos en lineas a, b, c ---
    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
#--------------------------------------------------------------------
# %%
#
import lote
c = lote.MiLote("Banana" , 100 , 56)
print(c.costo())

# %%
import lote
d = lote.Lote("mandarina" , 50 , 60)
print(d.CostoInflado())
# %%
