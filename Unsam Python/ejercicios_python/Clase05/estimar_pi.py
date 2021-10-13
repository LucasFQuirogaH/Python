"""-------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 5.4: Calcular pi
Escribí un programa estimar_pi.py que genere cien mil puntos aleatorios con la función generar_punto(), calcule la proporción de estos puntos
que caen en el círculo unitario (usando ¿x^2 + y^2 < 1?) y use este resultado para dar una aproximación de pi.
-------------------------------------------------------------------------------------------------------------------------------------------"""
#------------------------------- FUNCIONES -------------------------------
# FUNCION GENERAR PUNTO -------------------------------------------------- 
# def generar_punto(N):
#     import random
#     ListaDePuntos = []
#     for i in range(N):
#         ListaDePuntos.append((random.random() , random.random()))
#     return ListaDePuntos
# # MAIN -------------------------------------------------------------------
# ListadoDePuntos = []
# N = 100000
# M = 0
# ListadoDePuntos = generar_punto(N)

# for Punto in ListadoDePuntos:
#     if (Punto[0]**2 + Punto[1]**2) < 1:
#         M += 1
# print(f"Pi es aprimadamente: {4*M/N}")

"""-------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 5.5: Gaussiana

Con random.random() generamos valores aleatorios entre 0 y 1 con una distribución uniforme. En esa distribución, todos los valores posibles
tienen la misma probabilidad de ser seleccionados. También es posible generar valores aleatorios con otras distribuciones. Una de las
distribuciones más importantes es la distribución normal o Gaussiana.

La distribución normal tiene dos parámetros, denominados media y desvío estándar y denotados usualmente con las letras griegas mu y sigma,
respectivamente.
-------------------------------------------------------------------------------------------------------------------------------------------"""