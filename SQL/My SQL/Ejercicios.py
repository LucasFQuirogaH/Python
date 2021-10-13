# %%
# Conectamos y creamos la tabla...
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS peliculas(
                titulo varchar(20),
                actor varchar(20),
                duracion integer,
                cantidad integer
)""")
# %%
# Cargamos las peliculas...
cursor.execute("""INSERT INTO peliculas (titulo, actor, duracion, cantidad)
                VALUES ('Mision imposible','Tom Cruise',120,3)""")
cursor.execute("""INSERT INTO peliculas (titulo, actor, duracion, cantidad)
                VALUES ('Mision imposible 2','Tom Cruise',180,2)""")
cursor.execute("""INSERT INTO peliculas (titulo, actor, duracion, cantidad)
                VALUES ('Mujer bonita','Julia R.',90,3)""")
cursor.execute("""INSERT INTO peliculas (titulo, actor, duracion, cantidad)
                VALUES ('Elsa y Fred','China Zorrilla',90,2)""")
# %%
cursor.execute("SELECT * FROM peliculas")
for pelicula in cursor:
    print(pelicula)
# %%
# Mostrar algunas cosas
cursor.execute("SELECT  ")