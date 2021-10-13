#--------------------------------------------------------------------
# %%
#
import datetime
#--------------------------------------------------------------------
# %%
#
from datetime import datetime
print(datetime.now())
#--------------------------------------------------------------------
# %%
#
print(datetime.datetime.now())
#--------------------------------------------------------------------
# %%
#
datetime.date.today()
#--------------------------------------------------------------------
# %%
#
print(datetime.date.today())
# %%
print(dir(datetime))
# %%
dir(datetime)
# %%
help(datetime)
# %%
print(datetime.date(2019, 4, 13))
# %%
import datetime
timestamp = datetime.date.fromtimestamp(1326244364)
print('Fecha =', timestamp)

# %%
from datetime import date

hoy = date.today()

print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Día actual:', hoy.day)
print('Día de la semana:', hoy.weekday()) # va de 0 a 6 empezando en lunes

# %%
import os
import datetime
import time
#--------------------------------------------------------------------
camino = 'C:\\Users/Usuario/Downloads/Ejercicios/ejercicios_python/Clase01/rebotes.py'
#--------------------------------------------------------------------
# %%
#
stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))
#--------------------------------------------------------------------
# %%
#
fecha_acceso = datetime.datetime(year = 2017, month = 9, day = 21, hour = 19, minute =51, second = 0)
fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute =9, second = 24)
#--------------------------------------------------------------------
# %%
#
ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()
os.utime(camino, (ts_acceso, ts_modifi))
#--------------------------------------------------------------------
# %%
#
stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))
