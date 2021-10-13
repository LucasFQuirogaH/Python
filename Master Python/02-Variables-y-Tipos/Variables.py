"""
Una variable es un contenedor de informacion
que dentro guardara un dato, se puede crear
muchas variables y qque cada una tenga un dato distinto
"""
#Hemos creado variables 
#---------------------------------------------------------------------------------

""" texto = "Master en Python"
texto2 = "Yo soy Lucas Quiroga"
numero = 16000000
print(texto)
print(texto2)
print(numero) """

#Vamos a concatenar
#-----------------------------------------------------------------------------------
Nombre = "Lucas Fernando"
Apellido = "Quiroga"
Mensaje = "Voy a ganar mis USD 16.000.000"

#Otra forma de concatenar
print (Nombre + " " + Apellido + " " + Mensaje)

#Otra forma de concatenar
print (f"{Nombre} {Apellido} {Mensaje}")

#Otra forma de concatenar
print ("Hola mi nombre es {} {} y {}".format(Nombre,Apellido,Mensaje))

#Otra forma de concatenar
print (Nombre, Apellido, Mensaje)
