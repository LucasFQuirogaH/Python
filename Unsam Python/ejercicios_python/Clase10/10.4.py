#--------------------------------------------------------------------
# %%
#
def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line
#--------------------------------------------------------------------
# %%
#
for line in open('C:\Python/Unsam Python/Data/camion.csv'):
    print(line , end = '')
# %%
for line in filematch('C:\Python/Unsam Python/Data/camion.csv' , 'Naranja'):
    print(line, end = '')

# %%
from Modurama import Lucquifer
for line in filematch('C:\Python/Unsam Python/Data/camion.csv' , 'Naranja'):
    print(line, end = '')

# %%
import os
os.getcwd()
os.chdir("C:\Python/Unsam Python/ejercicios_python/Modurama/")
from Lucquifer import filematch
os.chdir("C:\Python/Unsam Python/ejercicios_python/Clase10")

for line in filematch('C:\Python/Unsam Python/Data/camion.csv' , 'Naranja'):
    print(line, end = '')
# %%
