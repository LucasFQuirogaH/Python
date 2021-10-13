# %%
import datetime
# %%
fecha_hora = datetime.datetime.now()
# %%
print(fecha_hora)
# %%
fecha = datetime.date.today()
print(fecha)
# %%
print(dir(datetime))
# %%
d = datetime.date(2019, 4, 13)
print(d)
# %%
from datetime import date
timestamp = date.fromtimestamp(18885244364)
print('Fecha =', timestamp)
# %%
from datetime import date
hoy = date.today()
print('Año actual:', hoy.year)
print('Mes actual:', hoy.month)
print('Día actual:', hoy.day)
print('Día de la semana:', hoy.weekday())
# %%
from datetime import time
a = time()       # time(hour = 0, minute = 0, second = 0)
print('a =', a)

b = time(11, 34, 56)
print('b =', b)

c = time(hour = 11, minute = 34, second = 56)
print('c =', c)

d = time(11, 34, 56, 234566)  # time(hour, minute, second, microsecond)
print('d =', d)
# %%
from datetime import time
a = time(11, 34, 56)
print('hour =', a.hour)
print('minute =', a.minute)
print('second =', a.second)
print('microsecond =', a.microsecond)
# %%
from datetime import datetime
# datetime(year, month, day)
a = datetime(2020, 4, 21)
print(a)
# %%
from datetime import datetime
a = datetime(2021, 4, 21, 6, 53, 31, 342260)
print('año =', a.year)
print('mes =', a.month)
print('día =', a.day)
print('hora =', a.hour)
print('minuto =', a.minute)
print('timestamp =', a.timestamp())
# %%
from datetime import datetime, date
t1 = date(year = 2021, month = 4, day = 21)
t2 = date(year = 2020, month = 8, day = 23)
t3 = t1 - t2
print(t3)

t4 = datetime(year = 2020, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2021, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print(t6)

print('tipo de t3 =', type(t3))
print('tipo de t6 =', type(t6))

# %%
from datetime import timedelta
t1 = timedelta(weeks = 1, days = 2, hours = 1, seconds = 33)
t2 = timedelta(days = 6, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2
print('t3 =', t3)
# %%
from datetime import timedelta
t1 = timedelta(seconds = 21)
t2 = timedelta(seconds = 55)
t3 = t1 - t2
print(t3)
print(abs(t3)) #Tiempo que falta para llegar

# %%
# Podés obtener el tiempo medido en segundos usando el método total_seconds()
from datetime import timedelta
t = timedelta(days = 1, hours = 2, seconds = 30, microseconds = 100000)
print('segundos totales =', t.total_seconds())

"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R
------------------------------------------------------------------------------------------------------------"""
# %%
# Formato de fecha usando strftime()
from datetime import datetime
now = datetime.now()
t = now.strftime('%H:%M:%S')
print('hora:', t)

s1 = now.strftime('%m/%d/%Y, %H:%M:%S')
# en formato mm/dd/YY H:M:S
print('s1:', s1)

s2 = now.strftime('%d/%m/%Y, %H:%M:%S')
# en formato dd/mm/YY H:M:S
print('s2:', s2)

# %%
