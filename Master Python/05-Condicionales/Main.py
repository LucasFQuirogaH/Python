# Condicional IF

# Ejemplo 1

# color = "rojo"

# if color == "rojo":
#     print("el color es rojo")
# else:
#     print("El color no es rojo")


# Ejemplo 2

# colorFavorito = "azul"

# colorPreguntado = input("Adivina cual es mi color favorito: ")

# if colorPreguntado == "azul":
#     print("perfecto, si! ese es mi color")
# else:
#     print("no, ese no era mi color favorito")


# if colorPreguntado == "negro":
#     print("Me gusta el negro pero no es el favorito")
# else:
#     if colorPreguntado == "verde":
#             print("el verde significa que sos de Bandfield")
#     else:
#             print ("Ya ni la muelas")


# Operadores de comparacion
# == Igual
# != diferente
# < Mayor que
# > Menor que
# <= Mayor o igual que
# >= Menor o igual que
# and Y
# or O
# ! Negacion (va en uno por uno)
# Not NO (va en el total entre parentesis)

# Ejemplo 2

# year = input ("En que año estamos?")
# #Castear el valor porque lo que se ingresa por teclado se interpreta como string


# if int(year) >= 2021 :
#     print("estamos en 2021 en adelante")
# else:
#     print("esperemos que termine pronto")


#Ejemplo 4

# numeroIngresado = int (input("ingrese el dia, recuerde que es del 1 al 7:  "))

#If anidados

# if (numeroIngresado) == 1 :
#     print("El dia pulsado es Lunes")
# else:
#     if numeroIngresado == 2 :
#         print("El dia pulsado es Martes")
#     else:
#         if numeroIngresado == 3 :
#             print("El dia pulsado es Miercoles")
#         else:
#             if numeroIngresado == 4 :
#                 print("El dia pulsado es Jueves")
#             else:
#                 if numeroIngresado == 5 :
#                     print("El dia pulsado es Viernes")
#                 else:
#                     if numeroIngresado == 6 :
#                         print("El dia pulsado es Sabado")
#                     else:
#                         if numeroIngresado == 7 :
#                             print("El dia pulsado es Domingo")
#                         else :
#                             print("Ingreso un numero incorrecto")
                            

# if (numeroIngresado) == 1 :
#     print("El dia pulsado es Lunes")
# elif numeroIngresado == 2 :
#     print("El dia pulsado es Martes")
# elif  numeroIngresado == 3 :
#     print("El dia pulsado es Miercoles")
# elif numeroIngresado == 4 :
#     print("El dia pulsado es Jueves")
# elif numeroIngresado == 5 :
#     print("El dia pulsado es Viernes")
# elif numeroIngresado == 6 :
#     print("El dia pulsado es Sabado")
# elif numeroIngresado == 7 :
#     print("El dia pulsado es Domingo")
# else :
#     print("Ingreso un numero incorrecto")


###############################################Ejemplo 5

# edad = int(input("Ingrese la edad de la persona: "))

# if edad < 18 or edad > 65 :
#     print ("usted no puede trabajar")
# else :
#     print(" Usted puede trabajar")



###############################################Ejemplo 6

# pais = input ("Ingrese su pais, todo en minuscula: ")

# if pais == "alemania" or pais == "mexico" or pais == "españa" or pais == "argentina" :
#     print(f"En {pais} se habla español!!")
# else :
#     print(f"En {pais} no se habla español")



###############################################Ejemplo 7

# pais = input ("Ingrese su pais, todo en minuscula: ")

# if not (pais == "alemania" or pais == "mexico" or pais == "españa" or pais == "argentina") :
#     print(f"En {pais} no se habla español!!")
# else :
#     print(f"En {pais} se habla español")
    
    
###############################################Ejemplo 8    

pais = input ("Ingrese su pais, todo en minuscula: ")

if pais != "alemania" or pais != "mexico" or pais != "españa" or pais != "argentina" :
    print(f"En {pais} no se habla español!!")
else :
    print(f"En {pais} se habla español")
    
    
    
# if condicion 1

# elif condicion 2


