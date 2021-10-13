"""----------------------------------------------------------------------------------------------------------------------
Ejercicio 5.5: Gaussiana

agamos algún ejercicio sencillo antes de terminar. Supongamos que una persona se compra un termómetro que mide la
temperatura con un error aleatorio normal con media 0 y desvío estándar de 0.2 grados (error gaussiano). Si la
temperatura real de la persona es de 37.5 grados, simulá usando normalvariate() (con mu y sigma adecuados) n = 99 valores
medidos por el termómetro.

Imprimí los valores obtenidos en las mediciones de temperatura simuladas y luego, como resumen, cuatro líneas indicando
el valor máximo, el mínimo, el promedio y la mediana de estas n mediciones. Guardá tu programa en el archivo termometro.py.

Para encontrar el máximo y mínimo podés usar y agrandar tu código de busqueda_en_listas.py o usar las primitivas max()
y min() de Python. El promedio es la suma de los valores dividido su cantidad; podés programarla desde cero o usar la
primitiva sum() y un cociente por n. Finalmente, la mediana de una cantidad impar de valores es el valor en la posición
central cuando los datos están ordenados. Acá podés usar el método sort() de listas. Y ya que estamos, ¿se te ocurre cómo
encontrar los cuartiles?

----------------------------------------------------------------------------------------------------------------------"""
# import random
# import numpy
# N = 99
# mu = 32.5
# sigma = 0.2
# Mediciones = []

# for i in range(N):
#     Medicion = random.normalvariate(mu,sigma)
#     Mediciones.append(Medicion)
#     Medicion = 0
# Mediciones.sort()

# Promedio = (sum(Medicion for Medicion in Mediciones))/N
# Maximo = max(Mediciones)
# Minimo = min(Mediciones)
# Mediana = Mediciones[49]
# Tres = round(3*N/4)
# print(Tres)
# Q1 = Mediciones[round(N/4)]
# Q3 = Mediciones[round(3*N/4)]

# print("--- Resumen ---")
# print(f"Promedio:  {Promedio:>5.02f}")
# print(f"Máximo:    {Maximo:>5.02f}")
# print(f"Mínimo:    {Minimo:>5.02f}")
# print(f"Mediana:   {Mediana:>5.02f}")
# print(f"Cuartil 1: {Q1:>5.02f}")
# print(f"Cuartil 3: {Q3:>5.02f}")


"""-------------------------------------------------------------------------------------------------------------------
Ejercicio 5.7: Guardar temperaturas
Ampliá el código de termometro.py que escribiste en el Ejercicio 5.5 para que guarde el vector con las temperaturas
simuladas en el directorio Data de tu carpeta de ejercicios, en un archivo llamado Temperaturas.npy. Hacé que corra
999 veces en lugar de solo 99.

Ejercicio 5.8: Empezando a plotear
En un rato vamos a empezar a hacer gráficos con Python. Aquí solo un botón de muestra.

Escribí un archivo plotear_temperaturas.py que lea el archivo de datos Temperaturas.npy con 999 mediciones simuladas
que creaste recién y, usando el siguiente ejemplo, hacé un histograma de las temperaturas simuladas:
--------------------------------------------------------------------------------------------------------------------"""
import random
import numpy as np
import copy
N = 999
mu = 32.5
sigma = 0.2
Mediciones = []

for i in range(N):
    Medicion = random.normalvariate(mu,sigma)
    Mediciones.append(Medicion)
    Medicion = 0
Mediciones.sort()

Promedio = (sum(Medicion for Medicion in Mediciones))/N
Maximo = max(Mediciones)
Minimo = min(Mediciones)
Mediana = Mediciones[49]
Tres = round(3*N/4)
print(Tres)
Q1 = Mediciones[round(N/4)]
Q3 = Mediciones[round(3*N/4)]

print("--- Resumen ---")
print(f"Promedio:  {Promedio:>5.02f}")
print(f"Máximo:    {Maximo:>5.02f}")
print(f"Mínimo:    {Minimo:>5.02f}")
print(f"Mediana:   {Mediana:>5.02f}")
print(f"Cuartil 1: {Q1:>5.02f}")
print(f"Cuartil 3: {Q3:>5.02f}")

Temperaturas = np.array(Mediciones)
np.save("Data/Temperaturas" , Temperaturas)