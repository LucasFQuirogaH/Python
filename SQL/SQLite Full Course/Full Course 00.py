#--------------------------------------------------------------------
# %%
#
import sqlite3
import os
from sqlite3.dbapi2 import Connection
os.chdir('C:\\Python/SQL/SQLite Full Course')
#--------------------------------------------------------------------
# # Conexion que se borra cuando finaliza el programa
# ConexionTemporal = sqlite3.connect(':memory:')
# #--------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
#
conexion = sqlite3.connect('customer.db')
#--------------------------------------------------------------------
# Crear un cursor
cursor = conexion.cursor()
#--------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
# Crear una tabla
try:
    conexion.execute(""" Create table Clientes(
                    Nombre text,
                    Apellido text,
                    Email text
                )""")
except sqlite3.OperationalError:
    print('Ya existe')
#--------------------------------------------------------------------
# Tipos de datos
# NULL
# INTEGER
# REAL
# TEXT
# BLOB El valor es una masa de datos, almacenada exactamente como se ingresó
#--------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
# Insertamos datos
conexion = sqlite3.connect('customer.db')
conexion.execute('Insert into Clientes (Nombre , Apellido , Email) Values (? , ? , ?)' ,('Lucas' , 'Quiroga' , 'lucquifer@gmail.com'))
conexion.commit()
conexion.close()
#--------------------------------------------------------------------
# %%
# Otra manera directa
conexion = sqlite3.connect('customer.db')
conexion.execute("Insert into Clientes values ('Marcela' , 'Fragale' , 'marcelafragale@gmail.com')")
conexion.commit()
conexion.close()
# %%
# Insertar varios de una vez
import sqlite3
ClientesVarios = [
                    ('Juan' , 'Fernandez' , 'jfernandez@yahoo.com'),
                    ('Marcelo' , 'Romero' ,'marce56@hotmail.com'),
                    ('Pedro' , 'Picapiedra' , 'pp@antes.com'),
                    ('Harry' , 'Familia' , 'harrydebemorir@yahoo.com.ar')
                ]
conexion = sqlite3.connect('customer.db')
conexion.executemany("Insert into Clientes values (? , ? , ?)" , ClientesVarios)
conexion.commit()
conexion.close()
# %%
# Consultar Todos los datos
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
pprint((conexion.execute("Select * from clientes")).fetchall())
conexion.commit()
conexion.close()
# %%
# Consultar uno (El primero)
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
pprint((conexion.execute("Select * from clientes")).fetchone())
conexion.commit()
conexion.close()
# %%
# Consultar varios pero no todos
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
pprint((conexion.execute("Select * from clientes")).fetchmany(3))
conexion.commit()
conexion.close()
# %%
# Todos en rebanadas
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
Items = (conexion.execute("Select * from clientes")).fetchall()
for item in Items:
    print(item[0])
conexion.commit()
conexion.close()
# %%
# Colocar un indice temporal
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
Items = (conexion.execute("Select rowid, * from clientes")).fetchall()
for item in Items:
    print(item)
conexion.commit()
conexion.close()
# %%
# Buscar en especifico de acuerdo al apellido por ejemplo
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
print((conexion.execute("Select * from clientes where Apellido = 'Picapiedra'")).fetchall())
conexion.commit()
conexion.close()
# %%
# Buscar en especifico de acuerdo al apellido con asterisco
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
pprint((conexion.execute("Select * from clientes where Nombre like 'Ma%'")).fetchall())
conexion.commit()
conexion.close()
# %%
# Actualizar datos en una linea
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
conexion.execute("""Update Clientes set Nombre = 'Fernando' where Apellido = 'Quiroga' """)
pprint((conexion.execute("Select * from clientes")).fetchall())
conexion.commit()
conexion.close()
# %%
# Actualizar datos en una linea usando la misma columna
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
conexion.execute("""Update Clientes set Nombre = 'Lucas' where Nombre = 'Fernando' """)
conexion.execute("""Update Clientes set Apellido = 'Quiroga' where Apellido = 'Herrera' """)
pprint((conexion.execute("Select * from clientes")).fetchall())
conexion.commit()
conexion.close()
# %%
# Actualizar datos en una linea usando el ID
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
conexion.execute("""Update Clientes set Nombre = 'Lucas' where rowid = 1 """)
pprint((conexion.execute("Select * from clientes")).fetchall())
conexion.commit()
conexion.close()
# %%
# Borrar un registro
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
conexion.execute("""Delete from Clientes where rowid = 2 """)
pprint((conexion.execute("Select * from clientes")).fetchall())
conexion.commit()
conexion.close()
# %%
# Ordenar un registro
# Con el For Muestra el indice
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
items = (conexion.execute("""Select  * from Clientes order by Apellido asc""")).fetchall()
#--------------------------------------------------------------------
for item in items:
    print(item)
#--------------------------------------------------------------------
conexion.commit()
conexion.close()
# %%
# Muestra Ordenar un registro descendente
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
pprint((conexion.execute("""Select  * from Clientes order by Apellido desc""")).fetchall())
#--------------------------------------------------------------------
conexion.commit()
conexion.close()
# %%
# Muestra Ordenado un registro ascendente
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
pprint((conexion.execute("""Select  * from Clientes order by Apellido asc""")).fetchall())
#--------------------------------------------------------------------
conexion.commit()
conexion.close()
# %%
# Muestra Ordenado un registro ascendente y colocasel rowid adelante
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
pprint((conexion.execute("""Select rowid,  * from Clientes order by Apellido asc""")).fetchall())
conexion.commit()
conexion.close()
# %%
# AND
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
pprint((conexion.execute("""Select rowid, * from Clientes where Nombre like 'Mar%' and Apellido like 'Fr%'""")).fetchall())
conexion.commit()
conexion.close()
# %%
# OR
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
pprint((conexion.execute("""Select rowid, * from Clientes where Nombre like 'Mar%' or Nombre like 'H%'""")).fetchall())
conexion.commit()
conexion.close()
# %%
# Limitar a 2, mostrar solo 2 en orden descendente
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
pprint((conexion.execute("""Select rowid, * from Clientes order by rowid desc limit 2""")).fetchall())
conexion.commit()
conexion.close()
# %%
# Limitar a 2, mostrar solo 2.
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
pprint((conexion.execute("""Select rowid, * from Clientes limit 2""")).fetchall())
conexion.commit()
conexion.close()
# %%
# Eliminar una tabla completa
import sqlite3
from pprint import pprint
conexion = sqlite3.connect('customer.db')
conexion.execute("""Drop table Clientes""")
conexion.commit()
conexion.close()
# %%
