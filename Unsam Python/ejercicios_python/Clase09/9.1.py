#--------------------------------------------------------------------
# %%
# Imports
import lote
#--------------------------------------------------------------------
# %%
# Probando
a = lote.Lote("Pera" , 100 , 490.10)
# %%
b = lote.Lote("Manzana" , 50 , 122.34)
c = lote.Lote("Naranja" , 75 , 91.75)
#--------------------------------------------------------------------
# %%
#
a.precio
a.nombre
a.cajones
# %%
a.costo()
# %%
a.vender(25)
# %%
import fileparse
with open('C:\Python/Unsam Python/Data/camion.csv') as lineas:
    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
# %%
# 9.3
import fileparse
with open('C:\Python/Unsam Python/Data/camion.csv') as lineas:
    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
camion = [ lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
print(camion)
# %%
sum([c.costo() for c in camion])
# %%
