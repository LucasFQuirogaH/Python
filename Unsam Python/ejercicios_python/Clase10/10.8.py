# %% [markdown]
# # Funciones
# ## Retroceder Nunca, Rendirse Jamas..
# **Corriendo**
def filematch(lines, substr):
    for line in lines:
        if substr in line:
            yield line
#--------------------------------------------------------------------
# %% [markdown]
# # Main
# ## Retroceder Nunca, Rendirse Jamas..
# **Esperando las naranjas**
from vigilante import vigilar
lines = vigilar('C:\Python/Unsam Python/Data/mercadolog.csv')
naranjas = filematch(lines, 'Naranja')
for line in naranjas:
    print(line)
#--------------------------------------------------------------------
# %%
#
from vigilante import vigilar
import csv
lineas = vigilar('C:\Python/Unsam Python/Data/mercadolog.csv')
filas = csv.reader(lineas)
for fila in filas:
    print(fila)
# %%
