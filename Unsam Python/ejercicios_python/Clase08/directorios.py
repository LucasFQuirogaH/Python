
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R
------------------------------------------------------------------------------------------------------------"""
# %%
import os
import datetime
import time

camino = "C:\Python/Unsam Python/Data/Hola.txt"

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))

fecha_acceso = datetime.datetime(year = 2021, month = 9, day = 21, hour = 19, minute =51, second = 0)
fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute =9, second = 24)

ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()
os.utime(camino, (ts_acceso, ts_modifi))

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))

# %%
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R
------------------------------------------------------------------------------------------------------------"""