#--------------------------------------------------------------------
# %%
#
def recursiva(cadena, frase, indice = 0, posiciones = False):
# Devuelve una lista con las posiciones en donde se encuentra b dentro de a'''
    if not posiciones:
        posiciones = []
    if len(cadena) == len(frase):
        if frase[0 : ] in cadena[0:len(frase)]:
            posiciones.append(indice)
        return posiciones
    else:
        if frase[0 : ] in cadena[0 : len(frase)]:
            posiciones.append(indice)
        return recursiva(cadena[1 : ], frase, indice + 1 , posiciones)
#--------------------------------------------------------------------
# %%
#
posiciones = recursiva("Hola Mundo" , "Mun")
print(posiciones)
# %%

"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
# Funcion del triangulo de tartaglia
def pascal(n , k):
    if n == 0:
        res = 1
    else:
        if k == 0:
            res = pascal(n - 1 , k)
        elif k == n:
            res = pascal(n - 1 , k - 1)
        else:
            res = pascal(n - 1 , k - 1) + pascal(n - 1 , k)
    return res