#--------------------------------------------------------------------
# %%
# Metodo de la burbuja
def ord_burbujeo(lista):
    for NumeroDePasada in range(len(lista) - 1 , 0 , -1):
        for i in range(NumeroDePasada):
            if lista[i] > lista[i + 1]:
                lista[i] , lista[i + 1] = lista[i + 1] , lista[i]
                print("DEBUG: ", lista)
#--------------------------------------------------------------------
lista = [0 , 9 , 3 , 8 , 5 , 3 , 2 , 4]
ord_burbujeo(lista)
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
# Metodo recursivo
# def ord_burbujeo(lista):
#     NumeroDePasada = len(lista) - 1
#     def RecursivaAuxiliar(lista , NumeroDePasada):
#         if NumeroDePasada == 0:
#             return lista
#         else:
#             for i in range(NumeroDePasada):
#                 if lista[i] > lista[i + 1]:
#                     lista[i] , lista[i + 1] = lista[i + 1] , lista[i]
#                     print("DEBUG: ", lista)
#             RecursivaAuxiliar(lista , (NumeroDePasada - 1))
#         return lista
#     lista = RecursivaAuxiliar(lista , NumeroDePasada)
#     return lista
#--------------------------------------------------------------------
lista = [0 , 9 , 3 , 8 , 5 , 3 , 2 , 4]
ord_burbujeo(lista)
# %%
