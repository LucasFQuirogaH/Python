# # ------------------------------------------------------- Funciones  --------------------------------------------------
# # def nombreDeMiFuncion()

# # y para llamarla

# # nombreDeLaFuncion(parametro)
# """-------------------------------------Definicion de la funcion----------------------------------------"""
# def muestraNombre () :
#     print("Hola me presento, Me llamo Lucas Quiroga y tengpo USD 16000000")
#     print("Gabriel es mi amigo")
#     print("Fernando es mi amigo")

    
# print("Aqui estoy")
# """-------------------------------------Invocacion de la funcion----------------------------------------"""
# muestraNombre ()



# def mostrarMiNombre(nombre) :
#     print(f"Como le va {nombre}?")

# nombre = input("Como se llama usted? ")
# mostrarMiNombre(nombre)

# """--------------------------------------------Ejemplo 3---------------------------------------------------"""

# Definicion de tabla

# def tabla(multiplicador) :
#     print("\n")
#     print(f"TABLA DE MULTIPLICAR DE {multiplicador}")
#     for indice in range (1 , 10) :
#         print(f"{multiplicador} x {indice} = {multiplicador * indice}")
#     print("\n")

# # Main

# multiplicador = int(input("ingrese el multiplicador de la tabla que desea: "))
# tabla(multiplicador)

# """----------------------------------------------  Ejemplo 4  ---------------------------------------------------"""

# # Defincion de saludame

# def saludame(nombre) :
#     saludo = f"Hola {nombre}"
#     return (saludo)

# # Main

# print(saludame("Lucas Quiroga"))


# """----------------------------------------------  Ejemplo 4 ---------------------------------------------------"""

# Defincion de Calculadora

# def Calculadora (numero1 , numero2, basicas = False) :
    
#     if basicas == True:
         
#         cadena = f"La suma es {numero1 + numero2}"
#         cadena += "\n"
#         cadena += f"La resta es {numero1 - numero2}"
#         cadena += "\n"
#     else :
            
#         cadena = f"La suma es {numero1 + numero2}"
#         cadena += "\n"
#         cadena += f"La resta es {numero1 - numero2}"
#         cadena += "\n"
#         cadena += f"La multiplicacion es {numero1 * numero2}"
#         cadena += "\n"
#         cadena += f"La division es {numero1 / numero2}"
#         cadena += "\n"
        
#     return (cadena)

# # Main

# mostrar = Calculadora(100 , 50, True)

# print(mostrar)
# """----------------------------------------------  Ejemplo 5 ---------------------------------------------------"""

#Funciones

# def getNombre(nombre) :
#     textoNombre = f"Nombre: {nombre}"
#     return(textoNombre)

# def getApellido(apellido) :
#     textoApellido = f" Apellido: {apellido}"
#     return (textoApellido)

# def total (nombre , apellido) :
#     textoTotal = getNombre(nombre) + "\n" + getApellido(apellido)
#     return textoTotal
    
# # Main

# mostrar = total ("Lucas" , "Quiroga")
# print(mostrar)

#Funciones

# def getNombre(nombre) :
#     textoNombre = f"Nombre: {nombre}"
#     return(textoNombre)

# def getApellido(apellido) :
#     textoApellido = f" Apellido: {apellido}"
#     return (textoApellido)

# def total (nombre , apellido) :
#     print(getNombre(nombre) + "\n" + getApellido(apellido))
    
# # Main

# total("Lucas", "Quiroga")

# """----------------------------------------------  Ejemplo 5 ---------------------------------------------------"""

#Funcion reservada Lambda

dimeElAnio = lambda anio : f"El año es {anio}"

# Main

print(dimeElAnio(2021))

