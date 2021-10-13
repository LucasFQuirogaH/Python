#--------------------------------------------------------------------
# %%
#
import math
from math import pi
#--------------------------------------------------------------------
# a = math.sqrt(x)
# b = math.sin(x)
# c = math.cos(x)
# d = math.tan(x)
# e = math.log(x)
#--------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
#
math.sin(90 * pi / 180)
# %%
a = 'Hello world'
#--------------------------------------------------------------------
# %%
#
a[0]
#--------------------------------------------------------------------
# %%
#
a[4]
#--------------------------------------------------------------------
# %%
#
a[-1]
# %%
a[:5]
# %%
a[5:] # toma el inicio pero no toma el final, es igual que for
# %%
a = 'Hello' +' ' +  'World'
#--------------------------------------------------------------------
# %%
#
a
# %%
s = '  Hello               que              hacer'
#--------------------------------------------------------------------
# %%
#
s.strip() #
#--------------------------------------------------------------------
# %%
#
s
# %%
s = '  Hello '
#--------------------------------------------------------------------
# %%
#
s.strip()
# %%
s.replace('Hello' , 'Hallo')
# %%
# Teoria
# s.endswith(suffix)     # Verifica si termina con el sufijo
# s.find(t)              # Primera aparición de t en s (o -1 si no está)
# s.index(t)             # Primera aparición de t en s (error si no está)
# s.isalpha()            # Verifica si los caracteres son alfabéticos
# s.isdigit()            # Verifica si los caracteres son numéricos
# s.islower()            # Verifica si los caracteres son minúsculas
# s.isupper()            # Verifica si los caracteres son mayúsculas
# s.join(slist)          # Une una lista de cadenas usando s como delimitador
# s.lower()              # Convertir a minúsculas
# s.replace(old,new)     # Reemplaza texto
# s.split([delim])       # Parte la cadena en subcadenas
# s.startswith(prefix)   # Verifica si comienza con un sufijo
# s.strip()              # Elimina espacios en blanco al inicio o al final
# s.upper()              # Convierte a mayúsculas

#--------------------------------------------------------------------
# %%
#
s = 'Hello World'
#--------------------------------------------------------------------
# %%
#
s[1] = 'a' # Intento cambiar la 'e' por una 'a'
# %%
