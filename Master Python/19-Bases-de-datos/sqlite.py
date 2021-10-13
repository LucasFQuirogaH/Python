"""------------------------------------------------------------------------------------------------------------
Ing.Lucas F. Quiroga H. Fecha: 24/06/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------------------------------------------------
# %%
#
import sqlite3
#--------------------------------------------------------------------
# %%
# Creamos la conexion
conexion = sqlite3.connect('C:\\Python/Master Python/19-Bases-de-datos/pruebas.db')
#--------------------------------------------------------------------
# %%
# Creamos un cursor para manejar mejor
cursor = conexion.cursor()
#--------------------------------------------------------------------
# %%
# Creamos la tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos(" +
"id INTEGER PRIMARY KEY AUTOINCREMENT," +
"titulo VARCHAR(255)," +
"descripcion text," +
"precio int(255)" +
")")
#--------------------------------------------------------------------
# %%
# Guardar cambios
conexion.commit()
#--------------------------------------------------------------------
# %%
# Instertar Datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto' , 'Descripcion del producto' , 550) ")
conexion.commit()
#--------------------------------------------------------------------
# %%
# Listar los productos (Lectura de datos)
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()
for producto in productos:
    print(producto)
    # print(f"Nombre: {producto[1]}")
#--------------------------------------------------------------------
# %%
# Primer registro, o primer producto
producto = cursor.fetchone()
cursor.execute("SELECT titulo FROM productos;")
print(productos)
#--------------------------------------------------------------------
# %%
# Borrar los productos pero quedaron las cabeceras!
cursor.execute("DELETE FROM productos")
conexion.commit()
#--------------------------------------------------------------------
# %%
# Insertar productos de una vez !!!
productos = [
    ("Ordenador portatil" , "Buen pc " , 7000) ,
    ("telefono portatil" , "Buen telefono " , 140) ,
    ("Placa base" , "Buena placa" , 80) ,
    ("tablet 15" , "Buena tablet " , 300) ,
]
#--------------------------------------------------------------------
cursor.executemany("INSERT INTO productos VALUES (null , ? , ? , ?)" , productos)
conexion.commit()
#--------------------------------------------------------------------
# %%
#
# Listar los productos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()
for producto in productos:
    print(producto)
    print()
#--------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
# Para que filtre cuando los precios son mayores a 300
cursor.execute("SELECT * FROM productos WHERE precio > 300 ;")
#--------------------------------------------------------------------
# %%
# Cambiar de precios
cursor.execute("UPDATE productos SET precio=670 WHERE precio=80 ;")
#--------------------------------------------------------------------
# %%
# Cerrar
conexion.close()