#--------------------------------------------------------------------
# %%
#
camion = [
    ('Pera', 100, 490.1),
    ('Naranja', 50, 91.1),
    ('Caqui', 150, 83.44),
    ('Naranja', 100, 45.23),
    ('Pera', 75, 572.45),
    ('Lima', 50, 23.15)
]

#--------------------------------------------------------------------
# %%
#
from collections import Counter
total_cajones = Counter()
#--------------------------------------------------------------------
# %%
#
total_cajones
#--------------------------------------------------------------------
# %%
#
for nombre, n_cajones, precio in camion:
    total_cajones[nombre] += n_cajones
#--------------------------------------------------------------------
# %%
#
total_cajones['Naranja']     # 150
# %%
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
#
from collections import Counter
import csv
with open('C:\Python/Unsam Python/Data/camion.csv' , 'rt' , encoding = 'utf8') as lectura:
    camion = csv.reader(lectura)
    headers = next(camion)
    tenencias = Counter()
    for s in camion:
        tenencias[s[0]] += int(s[1])

    print(tenencias)

# %%
from collections import Counter
import csv
with open('C:\Python/Unsam Python/Data/camion.csv' , 'rt' , encoding = 'utf8') as lectura:
    camion = csv.reader(lectura)
    headers = next(camion)
    lista = []
    for linea in camion:
        lista.append(dict(zip(headers , linea)))
    tenencias = Counter()
    for s in lista:
        tenencias[s['nombre']] += int(s['cajones'])
    print(tenencias)
#--------------------------------------------------------------------------------------------------------------
# %%
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
listazip = list(zipped)
#--------------------------------------------------------------------
# %%
#
listazip
#--------------------------------------------------------------------
# %%
#
x2 , y2 = zip(*listazip)
#--------------------------------------------------------------------
# x2, y2 = zip(*zip(listazip))

# %%
x2
#--------------------------------------------------------------------
# %%
#
y2
# %%
