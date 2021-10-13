"""-------------------------------------------------------------------------------------------------------------------
Manejo de errores
-------------------------------------------------------------------------------------------------------------------"""
# try :
#     nombre= input ("Ingrese su nombre: ")
#     if len(nombre) > 1 :
#         nombre_de_usuario = "Su nombre es " + nombre
#     print(nombre_de_usuario)
# except :
#     print("Ocurrio un error")

# try:
#     numero = int(input("Ingrese un numero para elevarlo al cuadrado: "))
#     print(f"Su numero elevado al cuadrado es: {numero*numero}")
# except ValueError:
#     print ("Ingrese un valor correcto")
# except TypeError:
#     print ("Debe castear los valores")
# except Exception as e :
#     print("Se ha producido un error " + type(e).__name__)

bandera = 0
while bandera == 0 :
    try:
        nombre = input ("Introduce el nombre: ")
        edad = int(input ("Introduce la edad: "))
        if edad < 5 or edad > 110 :
            raise ValueError (" La edad que introdujo no es real")
        elif len(nombre) < 1:
            raise ValueError (" El nombre es muy corto")
        else :
            print("Bienvenido " + nombre)
            bandera = 1
    except ValueError :
        print("Introduzca los datos correctamente")


