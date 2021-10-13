"""----------------------------------------------------------------------------------------------------------------------
Ejercicio de SQLITE#
----------------------------------------------------------------------------------------------------------------------"""


import sqlite3
conexion = sqlite3.connect('Banco_Internacional/Stock_de_Celulares.db')
puntero =conexion.cursor()

puntero.execute("CREATE TABLE IF NOT EXISTS Telefonos (" +
"id INTEGER PRIMARY KEY AUTOINCREMENT," + 
"Celular VARCHAR (255)" + 
"Descripcion text" + 
"Precio int(255)" +
")")

conexion.commit()















# cursor = conexion.cursor()

# #Creamos tabla
# cursor.execute("CREATE TABLE IF NOT EXISTS productos(" +
# "id INTEGER PRIMARY KEY AUTOINCREMENT," +
# "titulo VARCHAR(255)," +
# "descripcion text," +
# "precio int(255)" +
# ")")

# #Guardar cambios
# conexion.commit()

# # Instertar Datos
# cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto' , 'Descripcion del producto' , 550) ")
# conexion.commit()

#Listar los productos
# cursor.execute("SELECT * FROM productos;")
# productos = cursor.fetchall()
# for producto in productos:
#     print(f"Nombre: {producto[1]}")

# producto = cursor.fetchone()    
# cursor.execute("SELECT titulo FROM productos;")
# print(productos)

# cursor.execute("DELETE FROM productos")
# conexion.commit()


# productos = [
#     ("Ordenador portatil" , "Buen pc " , 7000) , 
#     ("telefono portatil" , "Buen telefono " , 140) , 
#     ("Placa base" , "Buena placa" , 80) , 
#     ("tablet 15" , "Buena tablet " , 300) , 
# ]

# cursor.executemany("INSERT INTO productos VALUES (null , ? , ? , ?)" , productos)
# conexion.commit()

# #Listar los productos
# cursor.execute("SELECT * FROM productos;")
# productos = cursor.fetchall()
# for producto in productos:
#     print(f"Nombre: {producto[1]}")



# #Para borrar
# cursor.execute("DELETE * FROM productos")
# cursor.commit()


# #Cerrar la conexion
# conexion.close()
