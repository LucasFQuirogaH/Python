#--------------------------------------------------------------------
# %%
#
def bbinaria_rec(lista , e):
    res = False
    if len(lista) == 0:
        res = False
    # elif len(lista) == 1 and lista[0] == e:
    #     res = True
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista) // 2
        if e >= lista[medio]:
            res = bbinaria_rec(lista[medio : ] , e)
        if e < lista[medio]:
            res = bbinaria_rec(lista[ : medio] , e)
    return res
#--------------------------------------------------------------------
# %%
#
Resultado = bbinaria_rec([0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9] , 3)
print(Resultado)
# %%
