#--------------------------------------------------------------------
# %%
# Conectar
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "MasterPython"
)
#--------------------------------------------------------------------
# Crear la base de datos
cursor = database.cursor()
cursor.execute("Create database if not exists MasterPython")
#--------------------------------------------------------------------
cursor.execute("Show Databases")
for bd in cursor:
    print(bd)
#--------------------------------------------------------------------
# %%
# crear tabla
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "MasterPython"
)
#--------------------------------------------------------------------
cursor = database.cursor()
cursor.execute(""" create table if not exists Vehiculos(
                id int(10) auto_increment not null,
                marca varchar(40) not null,
                modelo varchar(40) not null,
                precio float(10,2) not null,
                constraint pk_vehiculo primary key(id)
)""")
# Tenes que colocar Show Tables para que luego las muestre
cursor.execute("Show Tables")
for table in cursor:
    print(table)
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------------------------------------------------
# %%
# Crear Base de Datos
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = ""
) # Sin nombre en data base porque la estas creando
cursor = database.cursor()
cursor.execute("Create database if not exists MasterPython")  # Lo que esta entre comillas es lo que va directo en mySQL
#--------------------------------------------------------------------------------------------------------------
# %% Borrar base de datos
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
) # Pones en database la base datos que vas a trabajar
cursor = database.cursor()
cursor.execute("DROP DATABASE administracion") # Lo que esta entre comillas es lo que va directo en mySQL Y ;
#--------------------------------------------------------------------
# %%
# Mostrar las bases de datos que hay
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = ""
)
cursor = database.cursor()
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)
#--------------------------------------------------------------------
# %%
# Mostrar las tablas de datos que hay
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("SHOW TABLES") # Esto con ;
for tb in cursor:
    print(tb)
#--------------------------------------------------------------------
# %%
# Describir la tabla en concreto
import mysql.connector
from pprint import pprint
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("DESCRIBE usuarios") # Esto con ;
for description in cursor:
    pprint(description)
#--------------------------------------------------------------------
# %%
# Borrar la tabla
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("Drop TABLE usuarios") # Esto con ;
#--------------------------------------------------------------------
# %%
# Crear la tabla
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
            Nombre varchar(30),
            Domicilio varchar (30),
            Telefono varchar (11)
)""") # Esto con ;
#--------------------------------------------------------------------
# %%
# Insertar los datos
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("INSERT INTO usuarios (Nombre , Domicilio , Telefono) VALUES ('Pedro Picapiedra' , 'Cabaña 1596 - Hudson' , '1128746315') ") # Esto con ;)
#--------------------------------------------------------------------
# %%
# Recuperar datos en la tabla
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("SELECT Nombre , Domicilio , Telefono FROM usuarios") # Esto con ;)
for fila in cursor:
    print(fila)
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
# importar datos y levantar con Pandas
import pandas as pd
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("SELECT Nombre , Domicilio , Telefono FROM usuarios")
df = pd.DataFrame(cursor)
# %%
print(df.head())
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
# Creamos una tabla Nueva
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("""create table libros(
	titulo varchar(40),
	autor varchar(20),
	editorial varchar(15),
	precio float,
	cantidad integer
)""")
#--------------------------------------------------------------------
# %%
# Insertar los datos
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("""INSERT INTO libros (titulo , autor , editorial , precio , cantidad)
        VALUES ('El aleph','Borges','Emece',45.50,100) """)
cursor.execute("""INSERT INTO libros (titulo , autor , editorial , precio , cantidad)
        VALUES ('Alicia en el pais de las maravillas','Lewis Carroll','Planeta',25,200) """)
cursor.execute("""INSERT INTO libros (titulo , autor , editorial , precio , cantidad)
        VALUES ('Matematica estas ahi','Paenza','Planeta',15.8,200) """)
#--------------------------------------------------------------------
# %%
# Recuperar solo algunos datos
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("SELECT titulo , precio FROM libros")
for fila in cursor:
    print(fila)
#--------------------------------------------------------------------
# %%
# Recuperar solo algunos si se da una condicion con Where
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("SELECT titulo , actor FROM peliculas WHERE titulo = 'Mision Imposible'")
for fila in cursor:
    print(fila)
#--------------------------------------------------------------------
# %%
# Recuperar solo algunos si se da una condicion con Where
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("SELECT * FROM peliculas WHERE actor<>'Tom Cruise'")
for fila in cursor:
    print(fila)
#--------------------------------------------------------------------
# %%
#
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
""" =	igual
    <>	distinto
    >	mayor
    <	menor
    >=	mayor o igual
    <=	menor o igual
"""
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
# Borramos registros
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("DELETE FROM usuarios") # Borro todo!!!
#--------------------------------------------------------------------
# %%
# Setea el borrado total de una vez con un solo comando
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("set SQL_SAFE_UPDATES = 0")
cursor.execute("DELETE FROM usuarios") # Borro todo!!!
#--------------------------------------------------------------------
# %%
# Setea el borrado total de una vez con un solo comando
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
cursor.execute("set SQL_SAFE_UPDATES = 1")
cursor.execute("DELETE FROM usuarios") # DA ERROR!!!
#--------------------------------------------------------------------
# %%
# FIJARSE EL ESTADO
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
#--------------------------------------------------------------------
cursor.execute("SELECT @@SQL_SAFE_UPDATES")
for i in cursor:
    print(i)
# %%
# CAMBIAR TODOS LOS VALORES EN UN CAMPO DETERMINADO EN TODA LA TABLA
#--------------------------------------------------------------------
#Conexion y cursor
import mysql.connector
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "administracion"
)
cursor = database.cursor()
#--------------------------------------------------------------------
cursor.execute("UPDATE usuarios SET clave = 'RealMadrid'")
#--------------------------------------------------------------------------------------------------------------
# %%
# Key autoincrementada
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "",
database = "administracion"
)
cursor = database.cursor()
#--------------------------------------------------------------------
cursor.execute("""create table medicamentos(
            codigo integer auto_increment,
            nombre varchar(20),
            laboratorio varchar(20),
            precio float,
            cantidad integer,
            primary key (codigo)
)""") # Podes agregar la variable codigo al primero que agregues y desde ahi incrementara
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
# Truncar tabla
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "",
database = "administracion"
)
cursor = database.cursor()
#--------------------------------------------------------------------
cursor.execute("truncate table libros") # Permite que se borre la tabla mas rapido
# y ademas reinicia el conteo de la key que se autoincrementa.
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
#
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "",
database = "administracion"
)
cursor = database.cursor()
#--------------------------------------------------------------------
cursor.execute("""sele table libros(
            codigo integer auto_increment,
            titulo varchar(20) not null,
            autor varchar(30),
            editorial varchar(15),
            precio float,
            primary key(codigo)
);""") # Colocas NO Null para indicar que es la unica que puede ser Nula.
# Igualmente se puede ingresar un = ''
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
# Unsigned
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "",
database = "administracion"
)
cursor = database.cursor()
#--------------------------------------------------------------------
cursor.execute("""create table libros(
            codigo integer unsigned auto_increment,
            titulo varchar(20) not null,
            autor varchar(30),
            editorial varchar(15),
            precio float unsigned,
            cantidad integer unsigned,
            primary key (codigo)
)""") # Se conoloca unsigned para que el rango de representacion se multiplique x2 y vas
# colocando reestricciones.
#--------------------------------------------------------------------------------------------------------------
# %%
# SQL Mode para poder escribir valores por defecto
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("SET sql_mode = ''")
#--------------------------------------------------------------------------------------------------------------
# %%
# Atributos varios
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("""create table if not exists libros(
            codigo int unsigned auto_increment,
            titulo varchar(20) not null,
            autor varchar(30) default 'desconocido',
            editorial varchar(15),
            precio decimal(5,2) unsigned default '1.11',
            cantidad mediumint unsigned not null,
            primary key(codigo)
);""")
# %%
# Aplicando Zerofill para que agregue ceros a la izquierda y rellene
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("""create table if not exists libros(
            codigo int zerofill auto_increment,
            titulo varchar(20) not null,
            autor varchar(30) default 'desconocido',
            editorial varchar(15),
            precio decimal(5,2) unsigned default '1.11',
            cantidad smallint zerofill,
            primary key(codigo)
);""")
#--------------------------------------------------------------------------------------------------------------
""""
select ord('A');
select char(65,66,67);
select concat('Hola,',' ','como esta?');
select concat_ws('-','Juan','Pedro','Luis');
select find_in_set('hola','como esta,hola,buen dia');
select length('Hola');
select locate('o','como le va');
select position('o' in 'como le va');
select position('o' in 'como le va');
select locate('ar','Margarita',3);
select instr('como le va','om');
select lpad('hola',10,'0');
select left('buenos dias',8);
select right('buenos dias',8);
select substring('Buenas tardes',3,5);
select substring('Buenas tardes' from 3 for 5);
select mid('Buenas tardes' from 3 for 5);
select substring('Margarita',4);
select substring('Margarita' from 4);
select substring_index( 'margarita','ar',2);
select substring_index( 'margarita','ar',-2);
select ltrim('     Hola     ');
select rtrim('   Hola   ');
select trim (leading '0' from '00hola00');
select trim (trailing '0' from '00hola00');
select trim (both '0' from '00hola00');
select trim ('0' from '00hola00'); 
select trim ('  hola  ');
select replace('xxx.mysql.com','x','w');
select repeat('hola',3);
select reverse('Hola');
select insert('buenas tardes',2,6,'xx');
select lower('HOLA ESTUDIAnte');
select lcase('HOLA ESTUDIAnte');
select upper('HOLA ESTUDIAnte');
select ucase('HOLA ESTUDIAnte');

-ord(caracter): Retorna el código ASCII para el caracter enviado como argumento. Ejemplo:

 select ord('A');
retorna 65.

-char(x,..): retorna una cadena con los caracteres en código ASCII de los enteros enviados como argumentos. Ejemplo:

 
 select char(65,66,67);
retorna "ABC".

-concat(cadena1,cadena2,...): devuelve la cadena resultado de concatenar los argumentos. Ejemplo:

select concat('Hola,',' ','como esta?');
retorna "Hola, como esta?".

-concat_ws(separador,cadena1,cadena2,...): "ws" son las iniciales de "with separator". El primer argumento especifica el separador que utiliza para los demás argumentos; el separador se agrega entre las cadenas a concatenar. Ejemplo:

 select concat_ws('-','Juan','Pedro','Luis');
retorna "Juan-Pedro-Luis".

-find_in_set(cadena,lista de cadenas): devuelve un valor entre de 0 a n (correspondiente a la posición), si la cadena envidada como primer argumento está presente en la lista de cadenas enviadas como segundo argumento. La lista de cadenas enviada como segundo argumento es una cadena formada por subcadenas separadas por comas. Devuelve 0 si no encuentra "cadena" en la "lista de cadenas". Ejemplo:

 select find_in_set('hola','como esta,hola,buen dia');
retorna 2, porque la cadena "hola" se encuentra en la lista de cadenas, en la posición 2.

-length(cadena): retorna la longitud de la cadena enviada como argumento. Ejemplo:

 select length('Hola');
devuelve 4.

- locate(subcadena,cadena): retorna la posición de la primera ocurrencia de la subcadena en la cadena enviadas como argumentos. Devuelve "0" si la subcadena no se encuentra en la cadena. Ejemplo:

 select locate('o','como le va');
retorna 2.

- position(subcadena in cadena): funciona como "locate()". Devuelve "0" si la subcadena no se encuentra en la cadena. Ejemplo:

 select position('o' in 'como le va');
retorna 2.

- locate(subcadena,cadena,posicioninicial): retorna la posición de la primera ocurrencia de la subcadena enviada como primer argumentos en la cadena enviada como segundo argumento, empezando en la posición enviada como tercer argumento. Devuelve "0" si la subcadena no se encuentra en la cadena. Ejemplos:

 select locate('ar','Margarita',1);
retorna 1.

 select locate('ar','Margarita',3);
retorna 5.

- instr(cadena,subcadena): retorna la posición de la primera ocurrencia de la subcadena enviada como segundo argumento en la cadena enviada como primer argumento. Ejemplo:

 select instr('como le va','om');
devuelve 2.

- lpad(cadena,longitud,cadenarelleno): retorna la cadena enviada como primer argumento, rellenada por la izquierda con la cadena enviada como tercer argumento hasta que la cadena retornada tenga la longitud especificada como segundo argumento. Si la cadena es más larga, la corta. Ejemplo:

 select lpad('hola',10,'0');
retorna "000000hola".

- rpad(cadena,longitud,cadenarelleno): igual que "lpad" excepto que rellena por la derecha.

- left(cadena,longitud): retorna la cantidad (longitud) de caracteres de la cadena comenzando desde la inquierda, primer caracter. Ejemplo:

 select left('buenos dias',8);
retorna "buenos d".

- right(cadena,longitud): retorna la cantidad (longitud) de caracteres de la cadena comenzando desde la derecha, último caracter. Ejemplo:

 select right('buenos dias',8);
retorna "nos dias".

- substring(cadena,posicion,longitud): retorna una subcadena de tantos caracteres de longitud como especifica en tercer argumento, de la cadena enviada como primer argumento, empezando desde la posición especificada en el segundo argumento. Ejemplo:

 select substring('Buenas tardes',3,5);
retorna "enas".

- substring(cadena from posicion for longitud): variante de "substring(cadena,posicion,longitud)". Ejemplo:

 select substring('Buenas tardes' from 3 for 5);
- mid(cadena,posicion,longitud): igual que "substring(cadena,posicion,longitud)". Ejemplo:

 select mid('Buenas tardes' from 3 for 5);
retorna "enas".

- substring(cadena,posicion): retorna la subcadena de la cadena enviada como argumento, empezando desde la posición indicada por el segundo argumento. Ejemplo:

 select substring('Margarita',4);
retorna "garita".

-substring(cadena from posicion): variante de "substring(cadena,posicion)". Ejemplo:

 select substring('Margarita' from 4);
retorna "garita".

-substring_index(cadena,delimitador,ocurrencia): retorna la subcadena de la cadena enviada como argumento antes o después de la "ocurrencia" de la cadena enviada como delimitador. Si "ocurrencia" es positiva, retorna la subcadena anterior al delimitador (comienza desde la izquierda); si "ocurrencia" es negativa, retorna la subcadena posterior al delimitador (comienza desde la derecha). Ejemplo:

 select substring_index( 'margarita','ar',2);
retorna "marg", todo lo anterior a la segunda ocurrencia de "ar".

 select substring_index( 'margarita','ar',-2);
retorna "garita", todo lo posterior a la segunda ocurrencia de "ar".

-ltrim(cadena): retorna la cadena con los espacios de la izquierda eliminados. Ejemplo:

 select ltrim('     Hola     ');
retorna

"Hola     "
.
- rtrim(cadena): retorna la cadena con los espacios de la derecha eliminados. Ejemplo:

 select rtrim('   Hola   ');
retorna

"   Hola"
.
-trim([[both|leading|trailing] [subcadena] from] cadena): retorna una cadena igual a la enviada pero eliminando la subcadena prefijo y/o sufijo. Si no se indica ningún especificador (both, leading o trailing) se asume "both" (ambos). Si no se especifica prefijos o sufijos elimina los espacios. Ejemplos:

 select trim('  Hola  ');
retorna 'Hola'.

 select trim (leading '0' from '00hola00');
retorna "hola00".

 select trim (trailing '0' from '00hola00');
retorna "00hola".

 select trim (both '0' from '00hola00');
retorna "hola".

 select trim ('0' from '00hola00');
retorna "hola".

 select trim ('  hola  ');
retorna "hola".

-replace(cadena,cadenareemplazo,cadenareemplazar): retorna la cadena con todas las ocurrencias de la subcadena reemplazo por la subcadena a reemplazar. Ejemplo:

 select replace('xxx.mysql.com','x','w');
retorna "www.mysql.com'.

-repeat(cadena,cantidad): devuelve una cadena consistente en la cadena repetida la cantidad de veces especificada. Si "cantidad" es menor o igual a cero, retorna una cadena vacía. Ejemplo:

 select repeat('hola',3);
retorna "holaholahola".

-reverse(cadena): devuelve la cadena invirtiendo el order de los caracteres. Ejemplo:

 select reverse('Hola');
retorna "aloH".

-inser(cadena,posicion,longitud,nuevacadena): retorna la cadena con la nueva cadena colocándola en la posición indicada por "posicion" y elimina la cantidad de caracteres indicados por "longitud". Ejemplo:

 select inser('buenas tardes',2,6,'xx');
retorna ""bxxtardes".

-lcase(cadena) y lower(cadena): retornan la cadena con todos los caracteres en minúsculas. Ejemplo:

 select lower('HOLA ESTUDIAnte');
retorna "hola estudiante".

 select lcase('HOLA ESTUDIAnte');
retorna "hola estudiante".

-ucase(cadena) y upper(cadena): retornan la cadena con todos los caracteres en mayúsculas. Ejemplo:

 select upper('HOLA ESTUDIAnte');
retorna "HOLA ESTUDIANTE".

 select ucase('HOLA ESTUDIAnte');
retorna "HOLA ESTUDIANTE".

-strcmp(cadena1,cadena2): retorna 0 si las cadenas son iguales, -1 si la primera es menor que la segunda y 1 si la primera es mayor que la segunda. Ejemplo:

 select strcmp('Hola','Chau');

"""
#--------------------------------------------------------------------------------------------------------------
# select 5/0;
# MySQL tiene algunas funciones para trabajar con números. Aquí presentamos algunas.

# RECUERDE que NO debe haber espacios entre un nombre de función y los paréntesis porque MySQL puede confundir una llamada a una función con una referencia a una tabla o campo que tenga el mismo nombre de una función.

# -abs(x): retorna el valor absoluto del argumento "x". Ejemplo:

#  select abs(-20);
# retorna 20.

# -ceiling(x): redondea hacia arriba el argumento "x". Ejemplo:

#  select ceiling(12.34),
# retorna 13.

# -floor(x): redondea hacia abajo el argumento "x". Ejemplo:

#  select floor(12.34);
# retorna 12.

# -greatest(x,y,..): retorna el argumento de máximo valor.

# -least(x,y,...): con dos o más argumentos, retorna el argumento más pequeño.

# -mod(n,m): significa "módulo aritmético"; retorna el resto de "n" dividido en "m". Ejemplos:

#  select mod(10,3);
# retorna 1.

#  select mod(10,2);
# retorna 0.

# - %: %: devuelve el resto de una división. Ejemplos:

#  select 10%3;
# retorna 1.

#  select 10%2;
# retorna 0.

# -power(x,y): retorna el valor de "x" elevado a la "y" potencia. Ejemplo:

#  select power(2,3);
# retorna 8.

# -rand(): retorna un valor de coma flotante aleatorio dentro del rango 0 a 1.0.

# -round(x): retorna el argumento "x" redondeado al entero más cercano. Ejemplos:

#  select round(12.34);
# retorna 12.

#  select round(12.64);
# retorna 13.

# -srqt(): devuelve la raiz cuadrada del valor enviado como argumento.

# -truncate(x,d): retorna el número "x", truncado a "d" decimales. Si "d" es 0, el resultado no tendrá parte fraccionaria. Ejemplos:

#  select truncate(123.4567,2);
# retorna 123.45;

#  select truncate (123.4567,0);
#--------------------------------------------------------------------------------------------------------------

# -adddate(fecha, interval expresion): retorna la fecha agregándole el intervalo especificado. Ejemplos: adddate('2006-10-10',interval 25 day) retorna "2006-11-04". adddate('2006-10-10',interval 5 month) retorna "2007-03-10".

# -adddate(fecha, dias): retorna la fecha agregándole a fecha "dias". Ejemplo: adddate('2006-10-10',25), retorna "2006-11-04".

# -addtime(expresion1,expresion2): agrega expresion2 a expresion1 y retorna el resultado.

# -current_date: retorna la fecha de hoy con formato "YYYY-MM-DD" o "YYYYMMDD".

# -current_time: retorna la hora actual con formato "HH:MM:SS" o "HHMMSS".

# -date_add(fecha,interval expresion tipo) y date_sub(fecha,interval expresion tipo): el argumento "fecha" es un valor "date" o "datetime", "expresion" especifica el valor de intervalo a ser añadido o substraído de la fecha indicada (puede empezar con "-", para intervalos negativos), "tipo" indica la medida de adición o substracción. Ejemplo: date_add('2006-08-10', interval 1 month) retorna "2006-09-10"; date_add('2006-08-10', interval -1 day) retorna "2006-09-09"; date_sub('2006-08-10 18:55:44', interval 2 minute) retorna "2006-08-10 18:53:44"; date_sub('2006-08-10 18:55:44', interval '2:3' minute_second) retorna "2006-08-10 18:52:41". Los valores para "tipo" pueden ser: second, minute, hour, day, month, year, minute_second (minutos y segundos), hour_minute (horas y minutos), day_hour (días y horas), year_month (año y mes), hour_second (hora, minuto y segundo), day_minute (dias, horas y minutos), day_second(dias a segundos).

# -datediff(fecha1,fecha2): retorna la cantidad de días entre fecha1 y fecha2.

# -dayname(fecha): retorna el nombre del día de la semana de la fecha. Ejemplo: dayname('2006-08-10') retorna "thursday".

# -dayofmonth(fecha): retorna el día del mes para la fecha dada, dentro del rango 1 a 31. Ejemplo: dayofmonth('2006-08-10') retorna 10.

# -dayofweek(fecha): retorna el índice del día de semana para la fecha pasada como argumento. Los valores de los índices son: 1=domingo, 2=lunes,... 7=sábado). Ejemplo: dayofweek('2006-08-10') retorna 5, o sea jueves.

# -dayofyear(fecha): retorna el día del año para la fecha dada, dentro del rango 1 a 366. Ejemplo: dayofyear('2006-08-10') retorna 222.

# -hour(hora): retorna la hora para el dato dado, en el rango de 0 a 23.

# Ejemplo: hour('18:25:09') retorna "18";

# -minute(hora): retorna los minutos de la hora dada, en el rango de 0 a 59.

# -monthname(fecha): retorna el nombre del mes de la fecha dada.

# Ejemplo: monthname('2006-08-10') retorna "August".

# -month(fecha): retorna el mes de la fecha dada, en el rango de 1 a 12.

# -now() y sysdate(): retornan la fecha y hora actuales.

# -period_add(p,n): agrega "n" meses al periodo "p", en el formato "YYMM" o "YYYYMM"; retorna un valor en el formato "YYYYMM". El argumento "p" no es una fecha, sino un año y un mes. Ejemplo: period_add('200608',2) retorna "200610".

# -period_diff(p1,p2): retorna el número de meses entre los períodos "p1" y "p2", en el formato "YYMM" o "YYYYMM". Los argumentos de período no son fechas sino un año y un mes. Ejemplo: period_diff('200608','200602') retorna 6.

# -second(hora): retorna los segundos para la hora dada, en el rango de 0 a 59.

# -sec_to_time(segundos): retorna el argumento "segundos" convertido a horas, minutos y segundos. Ejemplo: sec_to_time(90) retorna "1:30".

# -timediff(hora1,hora2): retorna la cantidad de horas, minutos y segundos entre hora1 y hora2.

# -time_to_sec(hora): retorna el argumento "hora" convertido en segundos.

# -to_days(fecha): retorna el número de día (el número de día desde el año 0).

# -weekday(fecha): retorna el índice del día de la semana para la fecha pasada como argumento. Los índices son: 0=lunes, 1=martes,... 6=domingo). Ejemplo: weekday('2006-08-10') retorna 3, o sea jueves.

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
# Seleccionar y mostrar ordenados por autor
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("SELECT titulo , autor FROM libros ORDER BY autor ASC")
#--------------------------------------------------------------------
# %%
# Centencias OR - AND
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("SELECT * FROM libros WHERE (autor = 'Borges') AND(precio <= 20)") # AMBAS CONDICIONES
cursor.execute("SELECT * FROM libros WHERE (autor = 'Borges') OR (editorial = 'Planeta')") #Y/O
cursor.execute("SELECT * FROM libros WHERE (autor = 'Borges') XOR(precio <= 20)") # UNO U OTRO PERO NO LOS 2 A LA VEZ
cursor.execute("SELECT * FROM libros WHERE NOT (autor = 'Borges')") # INVIERTE LA CONDICION
#--------------------------------------------------------------------
# %%
# Comandos Between - in
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("SELECT * FROM libros WHERE autor in ('Borges' , 'Paenza')") #SI EL AUTOR ES UNO DE ESOS DENTRO DE LOS PARENTESIS
cursor.execute("SELECT * FROM libros WHERE precio BETWEEN 20 AND 40") #ENTRE ESOS 2 VALORES
#--------------------------------------------------------------------
# %%
# Comandos Like y not like que sustituye el * en las busquedas en windows
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("SELECT * FROM libros WHERE autor like %Borges%")
cursor.execute("SELECT * FROM libros WHERE autor not like %Borges%")
#--------------------------------------------------------------------
# %%
# Comando Regexp mas poderosa que like que tmabien busca
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("SELECT * FROM libros WHERE titulo REGEXP 'Ma'")
#--------------------------------------------------------------------
# %%
# Count, sum, max , min y avg
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("SELECT COUNT(*) FROM libros WHERE autor = 'Borges'")
cursor.execute("SELECT COUNT(precio) FROM libros WHERE autor = 'Borges'") #Cuenta los que tienen precio no null
#--------------------------------------------------------------------
cursor.execute("SELECT MAX(precio) FROM libros WHERE autor = 'Borges'") # MAXIMO
#--------------------------------------------------------------------
cursor.execute("SELECT MIN(precio) FROM libros WHERE autor = 'Borges'") # MINIMO
#--------------------------------------------------------------------
cursor.execute("SELECT AVG(precio) FROM libros WHERE titulo like '%PHP%'") #PROMEDIO DE LOS PRECIOS
#--------------------------------------------------------------------------------------------------------------
# %%
# group by
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("SELECT editorial , SUM(cantidad) FROM libros GROUP BY editorial") #Agrupa por editorial y permite hacer hacer una operacion
for item in cursor:
    print(item)
# %%
# Having es como un where para un Group by
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("SELECT editorial , COUNT(*) FROM libros GROUP BY editorial HAVING COUNT(*) > 2")
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
# alias, podes colocar nombre a la columna para que se muestre el alias en lugar de count por ejemplo
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("select count(*) as 'Los de Borges' from libros where autor like '%Borges%'")
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
# Primary key
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute(""" create table libros(
        codigo int unsigned auto_increment,
        titulo varchar(40) not null,
        autor varchar(30),
        editorial varchar(15),
        primary key(codigo)
);""")
cursor.execute("show index from libros") #Muestra quien es el key
#--------------------------------------------------------------------
# Index 
cursor.execute(""" create table libro(
        codigo int unsigned auto_increment,
        titulo varchar(40) not null,
        autor varchar(30),
        editorial varchar(15),
        primary key(codigo),
        index i_editorial (editorial)
);""")
#--------------------------------------------------------------------
# index compuesto
cursor.execute(""" create table libro(
        codigo int unsigned auto_increment,
        titulo varchar(40) not null,
        autor varchar(30),
        editorial varchar(15),
        primary key(codigo),
        index i_tituloeditorial (titulo,editorial)
);""")
#--------------------------------------------------------------------
# unique compuesto
cursor.execute(""" create table libro(
        codigo int unsigned auto_increment,
        titulo varchar(40) not null,
        autor varchar(30),
        editorial varchar(15),
        unique i_codigo(codigo),
        unique i_tituloeditorial (titulo,editorial)
);""")
#--------------------------------------------------------------------------------------------------------------
# Borrar los indices
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("DROP INDEX i_tituloeditorial ON libros")
#--------------------------------------------------------------------------------------------------------------
# Para crear index a tablas ya creadas sin colocar datos aun
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("create index i_editorial on libros (editorial);")
#--------------------------------------------------------------------------------------------------------------
# Recurperar tantos registros desde tal indice
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("select * from libros limit 5,4;") # Recupera 4 registros desde el registro 5
#--------------------------------------------------------------------------------------------------------------
# eliminar 2 registros con el precio mas bajo
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("delete from libros order by precio limit 2")
#--------------------------------------------------------------------------------------------------------------
# elimina 2 registros repetidos
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("delete from libros where titulo = 'El aleph' and autor = 'Borges' and editorial = 'Planeta' limit 2")
#--------------------------------------------------------------------------------------------------------------
# elegir 5 registros al azar
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("select * from libros order by rand() limit 5")
#--------------------------------------------------------------------------------------------------------------
# Reemplazar a traves de replace. Reemplaza conservando solo la primary key
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
# Lo va a reemplazar solo si existe el 23. Todos los otros campos seran reemplazados
cursor.execute("replace into libros values(23,'Java en 10 minutos','Mario Molina','Emece',25.5);")
# Funciona como inser si no especificas el key y le da un codigo.
cursor.execute("replace into libros values('Java en 10 minutos','Mario Molina','Emece',25.5);")
#--------------------------------------------------------------------------------------------------------------
# Agregar una nueva columna a una tabla que ya tiene valores
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
# Agrega la nueva columna con Null
cursor.execute("alter table libros add cantidad smallint unsigned")
# Agrega la nueva columna con valor por defecto 0
cursor.execute("alter table libros add cantidad smallint unsigned default 0")
# Para especificar luego de que columna debe ir la nueva que voy a agregar
cursor.execute("alter table libros add isbn smallint unsigned after titulo;")
#--------------------------------------------------------------------------------------------------------------
# Borrar columnas.
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("alter table libros drop edicion, drop columna")
#--------------------------------------------------------------------------------------------------------------
# Modificar la estructura de la columna
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("alter table libros modify edicion smallint unsigned")
#--------------------------------------------------------------------------------------------------------------
# Cambia el nombre de la columna y la estructura
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("alter table libros change titulo nombre varchar (40)")
#--------------------------------------------------------------------------------------------------------------
# Agregar index que no son primarios
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("alter table libros add index i_editorial (editorial)")
# para los indices unique
cursor.execute("alter table libros add unique index i_tituloeditorial (titulo,editorial)")
#--------------------------------------------------------------------------------------------------------------
# Borrar index de la tabla
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("alter table libros drop index i_editorial")
#--------------------------------------------------------------------------------------------------------------
# Renombrar las tablas
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("alter table amigos rename contactos")
# Otra opcion
cursor.execute("rename table amigos to contactos")
# Y si queres intercambiar los nombres habra que copiar la tabla
cursor.execute("rename table amigos to auxiliar, contactos to amigos, amigos to auxiliar")
#--------------------------------------------------------------------------------------------------------------
# Muestra por autor, cuenta las filas y agrupa por autor
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("""select autor, count(*)
        from libros
        group by autor
""")
#--------------------------------------------------------------------------------------------------------------
# Seleccion las filas y las cuenta. lueego agrupa por autor contando solo las que tengan 2 o mas.
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("""select autor, count(*)
        from libros
        group by autor
        having count(*)>1
""")
#--------------------------------------------------------------------------------------------------------------
# Selecciona por autor, peor con el if muestra solo las clausulas que salen en el mismo if. Agrupando por autor
# Muestra si son mas de 1 o 1.
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("""select autor,
        if (count(*)>1,'Más de 1','1')
        from libros
        group by autor
""")
#--------------------------------------------------------------------------------------------------------------
# Igual que con el if, muestra sus clausulas pero le pones nombre al count para luego ordenarlo por count a 
# traves del nombre.
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("""select autor,
        if (count(*)>1,'Más de 1','1') as cantidad
        from libros
        group by autor
        order by cantidad
""")
#--------------------------------------------------------------------------------------------------------------
# Case para diferentes situaciones. Muestra Legajo , promedio y estado en una tabla con los resultados
# del case
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("""select legajo,promedio,
            case truncate(promedio,0)
                when 0 then 'reprobado'
                when 1 then 'reprobado'
                when 2 then 'reprobado'
                when 3 then 'reprobado'
                when 4 then 'regular'
                when 5 then 'regular'
                when 6 then 'regular'
                when 7 then 'promocionado'
                when 8 then 'promocionado'
                when 9 then 'promocionado'
                else 'promocionado'
            end as 'estado'
            from alumnos
""")
#--------------------------------------------------------------------------------------------------------------
# Join para concatenar tablas que tienen una relacion
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("""select * from libros
        join editoriales
        on libros.codigoeditorial=editoriales.codigo
""") # Codigoeditorial y codigo es el mismo numero en ambas tablas, se relacionan asi
# Y luego debes especificar que columnas queres colcoar en la concatenacion para que se vea bien
# Luego tambien especificar a que tabla pertenece cada columna para evitar que haya un error 
# al haber 2 columnas con el mismo nombre en las 2 tablas.
#--------------------------------------------------------------------------------------------------------------
# Left Join para verificar de cuales editoriales no se tienen libros
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("""select * from editoriales 
        left join libros
        on editoriales.codigo = libros.codigoeditorial
""")
cursor.execute("""select editoriales.nombre , libros.titulo
        from editoriales
        left join libros
        on editoriales.codigo = libros.codigoeditorial
        where libros.codigoeditorial is not null
""")
#--------------------------------------------------------------------------------------------------------------
import mysql.connector
database = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "Administracion"
)
cursor = database.cursor()
cursor.execute("""ALTER TABLE
    Departamentos
DROP FOREIGN KEY
    Relacion;""") # Relacion es el nombre que se le coloca a la relacion cuando creas la forein Key
#--------------------------------------------------------------------------------------------------------------