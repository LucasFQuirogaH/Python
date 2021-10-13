"""---------------------------------------------------------------------------------------------------------------------
PRACTICA
---------------------------------------------------------------------------------------------------------------------"""
# FUNCIONES ------------------------------------------------------------------------------------------------------------
## FUNCION TIRAR -------------------------------------------------------------------------------------------------------
# def tirar():
#     import random
#     tirada = []
#     for i in range (5):
#         tirada.append(random.randint(1 ,6))
#     return tirada
# ## FUNCION ES GENERALA--------------------------------------------------------------------------------------------------
# def es_generala(Tirada):
#     Frecuencia = {}
#     for dado in Tirada:
#         if dado in Frecuencia:
#             Frecuencia[dado] += 1
#         else:
#             Frecuencia[dado] = 1
#     return Frecuencia

# # MAIN -----------------------------------------------------------------------------------------------------------------
# Tirada = []
# Tirada = tirar()
# print()
# print(es_generala(Tirada))

# FUNCIONES --------------------------------------------------------------------------------------------------------------
## FUNCION TIRAR ---------------------------------------------------------------------------------------------------------
# def tirar():
#     import random
#     tirada = []
#     for i in range (5):
#         tirada.append(random.randint(1 ,6))
#     return tirada
# ## FUNCION ES GENERALA----------------------------------------------------------------------------------------------------
# def es_generala(Tirada):
#     Contador = sum (1 for i in range((len(Tirada)) - 1) if Tirada[i] == Tirada[i + 1])
#     if Contador == 4:
#         return True
#     else:
#         return False


# MAIN -------------------------------------------------------------------------------------------------------------------
# N = 1000000
# G = sum(es_generala(tirar()) for i in range(N))
# print(G/N)
"""----------------------------------------------------------------------------------------------------------------------
¿Por qué varían más los resultados obtenidos con N = 100000 que con N = 1000000? PORQUE CUANDO EL N TIENDE A INFINITO LA
DISTRIBUCION SE HACE GAUSSEANA Y TIENE A ESTABILIZARSE LA PROBABILIDAD.
¿Cada cuántas tiradas en promedio podrías decir que sale una generala servida? CADA 1280 TIRADAS APROXIMADAMENTE.
¿Cómo se puede calcular la probabilidad de forma exacta? HACIENDO TENDER N A
----------------------------------------------------------------------------------------------------------------------"""
#Para generar la misma tirada
#random.seed(12365)
# import random
# def generar_punto():
#     x = random.random()
#     y = random.random()
#     return x,y
# print(generar_punto())


import numpy as np
a = np.array([1 , 2 , 3 , 4 , 5 , 6 , 7])
print(a)

np.zeros(2)
np.ones(2)
np.empty(2)
np.arange(4)
np.arange(2, 9, 2)
b = np.linspace(1 , 19 , num = 10 , dtype=np.int8)

vectorfila = a[np.newaxis, :]

#a = np.arange(1 , 20 , 2)
#b = np.linspace(1 , 19 , num = 10)
# ¿Qué diferencia hay en el resultado? Como muestra los valores. En uno coloca el valor entero. En el otro colcoca el
# valor con un punto.

# b = np.linspace(1 , 19 , num = 10 , dtype=np.int8)
# print(b)

# x = np.array([[1 , 2] , [3 , 4]])
# y = np.array([5 , 6])
# print(y)

# a = np.array([1, 2, 3, 4, 5, 6])
# print(a)
# print()
# print(np.shape(a))
# print(a.shape)
# vectorfila = a[np.newaxis, :]
# print(vectorfila)

# data = np.array([1, 2, 3])
# print(data[1])

# print(data[0:2])
# print(data[1:])
# print(data[-2:])

# a =np.array([[1 , 2 , 3 , 4] , [5 , 6 , 7 , 8] , [9 , 10 , 11 , 12]])
# print(a)
# print()
# five_up = (a < 5)
# print(a[five_up])

# five_up = (a > 5) | (a == 5)
# print((a > 5) | (a == 5))
# b = np.nonzero(a < 5)
# print(b)

# ListaDeCoordenadas = list(zip(b[0] , b[1]))
# print()
# print(ListaDeCoordenadas)

# b1 = a[0 , :]
# print(b1)
# b1[0] = 99
# print(a)

# b1 = copy.deepcopy(a[0 , :])
# b1 = a[0 , :].copy()
# print(b1)
# b1[0] = 99
# print(a)
# print()
# print(b1)

# data = np.array([1 , 2])
# ones = np.ones(2 , dtype = int)
# print(f"La suma es: {data + ones}")
# print()
# print(f"La resta es: {data - ones}")
# print()
# print(sum(data))

# b = np.array([[1, 1], [2, 2]])
# data = np.array([[1, 2], [3, 4], [5, 6]])
# print(data[2][0])
# (1/n) * np.sum (np.square(predictions - labes))

# b = np.array([[1, 1], [2, 2]])
# print(b)
# print()
# print(b.sum(axis=0))
# print()
# print(b.sum(axis=1))

# data = np.array([1.0, 2.0])
# print(data)
# print()
# print(1.6 * data)
# print()
# print(max(data))
# print()
# print(min(data))

#np.save('Data/Mis Matrices', a) Para Guardar archivos npy.
#b = np.load("Data/Mis matrices.npy") Para Cargar el archivo npy.
# b = np.load("Data/Mis matrices.npy")
# print(b)
# np.savetxt("Data/Mis matrices en txt.csv" , b) guardar csv
# c = np.loadtxt("Data/Mis matrices en txt.csv") cargar csv
# print(c)


# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4])
# plt.ylabel('some numbers')
# plt.show()
