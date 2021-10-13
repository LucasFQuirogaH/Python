#--------------------------------------------------------------------
# %%
#
import urllib.request
u = urllib.request.urlopen('http://www.youtube.com/')
data = u.read()
# %%
data
# %%
import Django
#--------------------------------------------------------------------
# %%
# Para Django
email_address = 'lucquifer@gmail.com'
if email_address:
    send_email(email_address, 'Hola como estas')
#--------------------------------------------------------------------
# %%
#
s = {
    'fruta': 'Manzana',
    'cajones': 100,
    'precio': 490.1
}
# %%
s
# %%
del s['fruta']
# %%
s
# %%
fila = ['Lima', '100', '32.2']
# %%
t = (fila[0], int(fila[1]), float(fila[2]))
# %%
t
# %%
nombre, cajones, precio = t
# %%
nombre
# %%
cajones
# %%
d = {'nombre': 'Lima', 'cajones': 75, 'precio':32.2, 'fecha': (14, 8, 2020), 'cuenta': 12345}
# %%
d
# %%
items = d.items()
# %%
items
# %%
texto = 'Palabra mas palabras mas palabras menos'
#--------------------------------------------------------------------
# %%
#
texto.split()
# %%
citricos = set(['Naranja', 'Limon', 'Mandarina'])
# %%
citricos
# %%
