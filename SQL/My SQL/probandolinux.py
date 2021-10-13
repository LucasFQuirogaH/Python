#--------------------------------------------------------------------
# %%
# borramos la tabla
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("drop table if exists UnaPrueba")
#--------------------------------------------------------------------
# %%
# creo la tabla
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("""create table libros(
            codigo int unsigned auto_increment,
            titulo varchar(20) not null,
            autor varchar(30) default 'desconocido',
            editorial varchar(15) default 'desconocida',
            precio decimal(5,2) unsigned default '1.11',
            cantidad mediumint unsigned not null,
            primary key(codigo)
);""")
#--------------------------------------------------------------------------------------------------------------
# %%
# 
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("SET sql_mode = ''")
cursor.execute("insert into libros (titulo,autor,precio) values ('El Elefante','Borges', 23.6)")
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
# Pruebo con otra cosa
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("""create table if not exists UnaPrueba(
            Nombre varchar(50),
            Telefono varchar(10)
)""")
#--------------------------------------------------------------------
# %%
# agregamos
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("""INSERT INTO UnaPrueba (Nombre , Telefono) VALUES ('Lucas Quiroga' , '1139290188');""")
# %%
