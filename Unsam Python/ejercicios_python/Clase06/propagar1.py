"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%



# Funciones ---------------------------------------------------------------------------------------------------
## FUNCIONES FUNCION PROPAGAR AL VECINO -----------------------------------------------------------------------
# %%
# def propagar_al_vecino(l):
#     modif = False
#     n = len(l)
#     for i,e in enumerate(l):
#         if e==1 and i<n-1 and l[i+1]==0:
#             l[i+1] = 1
#             modif = True
#         if e==1 and i>0 and l[i-1]==0:
#             l[i-1] = 1
#             modif = True
#     return modif

## FUNCIONES FUNCION BUSQUEDA LINEAL --------------------------------------------------------------------------
# %%
# def propagar(l):
#     m = l.copy()
#     veces=0
#     while propagar_al_vecino(l):
#         veces += 1
#     print(f"Repetí {veces} veces la función propagar_al_vecino.")
#     print(f"Con input {m}")
#     print(f"Y obtuve  {l}")
#     return m

## FUNCIONES FUNCION INCREMENTAR -----------------------------------------------------------------------------
# %%
# def incrementar(s):
#     carry = 1
#     l = len(s)
#     for i in range(l-1,-1,-1):
#         if (s[i] == 1 and carry == 1):
#             s[i] = 0
#             carry = 1
#         else:
#             s[i] = s[i] + carry
#             carry = 0
#     return s

# Main  --------------------------------------------------------------------------------------------------------
# %%
# propagar([0,0,0,0,1])
# propagar([0,0,1,0,0])
# propagar([1,0,0,0,0])

# %%
# print()
# print(incrementar([0,0,0,0,1]))



## FUNCIONES FUNCION INCREMENTAR -----------------------------------------------------------------------------
# %%
def incrementar(Secuencia):
    carry = 1
    l = len(Secuencia)
    for i in range(l-1,-1,-1):
        if (Secuencia[i] == 1 and carry == 1):
            Secuencia[i] = 0
            carry = 1
        else:
            Secuencia[i] = Secuencia[i] + carry
            carry = 0
    return Secuencia
## FUNCIONES FUNCION LISTAR SECUENCIAS -----------------------------------------------------------------------
# %%
def listar_secuencias(n):
    Secuencia = [0] * n
    Lista = []
    Lista.append(Secuencia.copy())
    Contador = 0
    while Contador < ((2**n)-1):
        Secuencia = incrementar(Secuencia)
        Contador += 1
        Lista.append(Secuencia.copy())
    return (Lista)

# Main  --------------------------------------------------------------------------------------------------------
# %%
print()
Lista = listar_secuencias(5)
print(Lista)