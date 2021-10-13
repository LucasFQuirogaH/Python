"""-----------------------------------------------------------------------------------------------------------------------
Ejercicio 5.1: Generala servida
Queremos estimar la probabilidad de obtener una generala servida (cinco Dados iguales) en una tirada de Dados. Podemos
hacer la cuenta usando un poco de teoría de probabilidades, o podemos simular que tiramos los Dados muchas veces y ver
cuántas de esas veces obtuvimos cinco Dados iguales. En este ejercicio vamos a usar el segundo camino.

Escribí una función tirar() que devuelva una lista con cinco Dados generados aleatoriamente. Escribí otra función
llamada es_generala(tirada) que devuelve True si y sólo si los cinco Dados de la lista tirada son iguales.

Luego analizá el siguiente código. Correlo con N = 100000 varias veces y observá los valores que obtenés. Luego
correlo algunas veces con N = 1000000 (ojo, hace un millón de experimentos, podría tardar un poco):
-----------------------------------------------------------------------------------------------------------------------"""
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

# # MAIN -------------------------------------------------------------------------------------------------------------------
# N = 1000000
# G = sum(es_generala(tirar()) for i in range(N))
# print(G/N)
"""----------------------------------------------------------------------------------------------------------------------
¿Por qué varían más los resultados obtenidos con N = 100000 que con N = 1000000? PORQUE CUANDO EL N TIENDE A INFINITO LA
DISTRIBUCION SE HACE GAUSSEANA Y TIENE A ESTABILIZARSE LA PROBABILIDAD.
¿Cada cuántas tiradas en promedio podrías decir que sale una generala servida? CADA 1280 TIRADAS APROXIMADAMENTE.
¿Cómo se puede calcular la probabilidad de forma exacta? HACIENDO TENDER N A INFINITO
----------------------------------------------------------------------------------------------------------------------"""

"""-----------------------------------------------------------------------------------------------------------------------
jercicio 5.2: Generala no necesariamente servida
Si uno juega con las reglas originales (se puede volver a tirar algunos de los cinco Dados hasta dos veces, llegando hasta
a tres tiradas en total) siguiendo una estrategia que intente obtener generala (siempre guardar los Dados que más se
repiten y tirar nuevamente los demás) es más probable obtener una generala que si sólo consideramos la generala servida.
Escribí un programa que estime la probabilidad de obtener una generala en las tres tiradas de una mano y guardalo en un
archivo generala.py.

Extra: Hay gente que, si en la primera tirada le salen todos Dados diferentes, los mete al cubilete y tira los cinco
nuevamente. Otras personas, eligen uno de esos Dados diferentes, lo guardan, y tiran sólo los cuatro restantes.
¿Podés determinar, por medio de simulaciones, si hay una de estas estrategias que sea mejor que la otra?
-----------------------------------------------------------------------------------------------------------------------"""
# FUNCIONES --------------------------------------------------------------------------------------------------------------

# FUNCION TIRAR ----------------------------------------------------------------------------------------------------------
# def tirar(Dados):
#     # Definiciones ----------------------------------------------------------
#     import random
#     # random.seed(13579) da la misma
#     from collections import Counter
#     UnaTirada = []
#     for i in range (Dados):
#         UnaTirada.append(random.randint(1 ,6))
#     tirada = Counter(UnaTirada).most_common()
#     return tirada

# ## FUNCION ES GENERALA----------------------------------------------------------------------------------------------------
# def es_generala(tirada):
#     GeneralaFull = []
#     OtrosDados = 0
#     while ((list(tirada[0])) == 1):
#         tirada = tirar(OtrosDados)
#     GeneralaFull = list(tirada[0])
#     if GeneralaFull[1] > 1:
#         if GeneralaFull[1] == 5: # Hay Generala
#             return True
#         elif GeneralaFull[1] == 4:
#             OtrosDados = 1
#         elif GeneralaFull[1] == 3:
#             OtrosDados = 2
#         elif GeneralaFull[1] == 2:
#             OtrosDados = 3
#     for i in range (2):
#         tirada = tirar(OtrosDados)
#         for tupla in tirada:
#             if tupla[0] == GeneralaFull[0]:
#                 GeneralaFull[1] += tupla [1]
#                 OtrosDados -= tupla[1]
#             if GeneralaFull[1] == 5:
#                 return True
#     return False

# # MAIN -------------------------------------------------------------------------------------------------------------------
# Dados = 5
# print(es_generala(tirar(Dados)))


# FUNCIONES --------------------------------------------------------------------------------------------------------------

# FUNCION TIRAR ----------------------------------------------------------------------------------------------------------
def tirar(Dados):
    # Definiciones ----------------------------------------------------------
    import random
    # random.seed(13579) da la misma
    from collections import Counter
    UnaTirada = []
    Caras = ["uno" , "dos" , "tres" , "cuatro" , "cinco" , "seis"]
    UnaTirada = (random.choices(Caras , k=5))
        
    tirada = Counter(UnaTirada).most_common()
    return tirada

## FUNCION ES GENERALA----------------------------------------------------------------------------------------------------
def es_generala(tirada):
    GeneralaFull = []
    OtrosDados = 0
    while ((list(tirada[0])) == 1):
        tirada = tirar(OtrosDados)
    GeneralaFull = list(tirada[0])
    if GeneralaFull[1] > 1:
        if GeneralaFull[1] == 5: # Hay Generala
            return True
        elif GeneralaFull[1] == 4:
            OtrosDados = 1
        elif GeneralaFull[1] == 3:
            OtrosDados = 2
        elif GeneralaFull[1] == 2:
            OtrosDados = 3
    for i in range (2):
        tirada = tirar(OtrosDados)
        for tupla in tirada:
            if tupla[0] == GeneralaFull[0]:
                GeneralaFull[1] += tupla [1]
                OtrosDados -= tupla[1]
            if GeneralaFull[1] == 5:
                return True
    return False

# MAIN -------------------------------------------------------------------------------------------------------------------
Dados = 5
print(es_generala(tirar(Dados)))