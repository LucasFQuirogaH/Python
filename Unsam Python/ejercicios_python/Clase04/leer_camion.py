"""---------------------------------------------------------------------------------------------------------------------------------------
POR LAS BARBAS DE MI ABUELO VAMOS!!!!!
---------------------------------------------------------------------------------------------------------------------------------------"""
# Creacionrom pprint import pprint
# import csv
# Creacion = open("Data/Creacionecha_camion.csv" , "r" , encoding = "utCreacion8")
# Lectura = csv.reader(Creacion)
# Cabeceras = next(Lectura)

# Seleccion = ["nombre" , "cajones" , "precio"]
# Indices = [Cabeceras.index(Linea) Creacionor Linea in Seleccion]


# ProximaLinea = next(Lectura)
# ElDiccionario = {Linea: ProximaLinea[index] Creacionor Linea , index in zip(Seleccion , Indices)}

# Camion = [{Linea: ProximaLinea[index] Creacionor Linea , index in zip(Seleccion , Indices)} Creacionor ProximaLinea in Lectura]
# pprint(Camion)

import csv

types = [str, int, float]

Creacion = open("Data/camion.csv")
Lectura = csv.reader(Creacion)
Cabecera = next(Lectura)
LineaActual = next(Lectura)

print("\n")
print(types[1](LineaActual[1])*types[2](LineaActual[2]))


r = list(zip(types, LineaActual))
print("\n")

convertido = []

# for Funcion, Valor in zip(types, LineaActual):
#     convertido.append(Funcion(Valor))

convertido = [Funcion(Valor) for Funcion , Valor in zip (types , LineaActual)]
print(convertido)


print(Cabecera)
print("\n")
print(convertido)
print("\n")
print(dict(zip(Cabecera, convertido)))

print({Nombre: Funcion(Valor) for Nombre , Funcion , Valor in zip(Cabecera , types , LineaActual)})
