# def RaizCuadrada (numero):
#     import math
#     RC_Resultado = math.sqrt(numero)
#     return(RC_Resultado)

# print(int(RaizCuadrada(25)))
# try:
#     assert isinstance(10, float)
# except AssertionError:
#     print("No va por ahi")
    
    
# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n:
#         if expresion[i] == 'a':
#             return True
#         else:
#             return False
#         i += 1

# rta = tiene_a ('palabra')
# print(rta)


# import csv
# from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion=[]
#     registro={}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1])
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#             registro = {}
#     return camion

# camion = leer_camion("Data/camion.csv")
# pprint(camion)


# Lista = [1 , 3 , 5 , 7 , 9]
# print(Lista.index(8))


# def busqueda_con_index(Lista, e):
#     if e in Lista:
#         pos = Lista.index(e)
#     else:
#         pos = -1
#     return pos


# # MAIN ---------------------------------------------------------
# while (1):
#     Lista = [1 , 3 , 5 , 7 , 9]
#     try:
#         ElValoror = int(input ("Ingrese el Valoror para buscar: "))
#         print((busqueda_con_index(Lista , ElValoror)))
#     except ValorueError:
#         print("Ingrese un numero correcto")


# a = [1, 2, 3, 4, 5]
# b = [2*x for x in a]
# print(b)


# a = [1, -5, 4, 2, -2, 10]
# b = [2*x for x in a if x > 0]
# print(b)

import csv
Creacion = open("Data/dowstocks.csv")
Lectura = csv.reader(Creacion)
Cabecera = next(Lectura)
LineaActual = next(Lectura)
 
# print(Cabecera)

# print(LineaActual)


types = [str, float, str, str, float, float, float, float, int]
convertido = [Funcion(Valor) for Funcion, Valor in zip(types, LineaActual)]

record = dict(zip(Cabecera, convertido))
print("\n")
print(record["date"])

aux = map(int , record["date"].split("/"))
print(tuple(aux))

