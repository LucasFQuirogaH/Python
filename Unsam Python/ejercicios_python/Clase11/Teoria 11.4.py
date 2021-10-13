# %%
#
def recursiva(numero):
    numero = str(numero)
    res = 0
    lista = [c for c in numero]
    def recursiva_aux(lista):
        res = 0
        if len (lista) == 1:
            return 1
        else:
            lista.pop(0)
            res = 1 + recursiva_aux(lista)
        return res
    res = recursiva_aux(lista)
    return res
#--------------------------------------------------------------------
# %%
#
print(recursiva(3521))
# %%
