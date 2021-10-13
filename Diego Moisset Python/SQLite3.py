#--------------------------------------------------------------------
# %%
#
import sqlite3
import os
#--------------------------------------------------------------------
# Cambiar directorio
os.chdir('C:\\Python/Diego Moisset Python/Python 287')
#--------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
# Crear la tabla
conexion = sqlite3.connect('bd1.db')
try:
    conexion.execute('''
        create table Articulos(
        Codigo integer primary key autoincrement,
        Descripcion text,
        Precio real
        )
    ''')
except sqlite3.OperationalError:
    print('Ya esta creada')
conexion.close()
#--------------------------------------------------------------------
# %%
# Insertar cosas ya
conexion = sqlite3.connect('bd1.db')
conexion.execute('Insert into Articulos(Descripcion , Precio) values (? , ?)' , ('Naranja' , 49.90))
conexion.execute('Insert into Articulos(Descripcion , Precio) values (? , ?)' , ('Manzana' , 58.36))
conexion.execute('Insert into Articulos(Descripcion , Precio) values (? , ?)' , ('Banana' , 53.21))
conexion.commit()
conexion.close()
# %%
# Mostrar las filas con for
conexion = sqlite3.connect('bd1.db')
Raw = conexion.execute('select Codigo , Descripcion , Precio from Articulos')
for fila in Raw:
    print(fila)
conexion.close()
# %%
# Consultar un articulo
conexion = sqlite3.connect('bd1.db')
Codigo = int(input('Ingrese el codigo'))
Producto = conexion.execute('select Descripcion, Precio from Articulos where Codigo = ?' , (Codigo ,))
fila = Producto.fetchone()
if fila != None:
    print(fila)
else:
    print('No existe el producto')
conexion.close()
# %%
# Recuperar varios datos de una vez
conexion = sqlite3.connect('bd1.db')
Precio = float(input('Ingrese el Precio'))
Productos = conexion.execute('select Descripcion, Precio from Articulos where Precio < ?' , (Precio ,))
filas = Productos.fetchall()
if len(filas) > 0:
    for fila in filas:
        print(fila)
else:
    print('No hay articulos con precio menor al ingresado')
conexion.close()
# %%
