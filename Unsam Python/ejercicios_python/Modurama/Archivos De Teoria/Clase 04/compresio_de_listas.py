#--------------------------------------------------------------------
# %%
#
a = [1, 2, 3, 4, 5]
b = [2 * x for x in a]
#--------------------------------------------------------------------
# %%
#
b
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
#
def leer_precios():
    OtroDicionario ={}
    Precios = {}
    Cabecera = []
    with open('C:\\Python/Unsam Python/Data/precios.csv', "rt" , encoding = "utf8") as creacion:
        Lectura = csv.reader(creacion)
        Cabecera = ["nombre" , "precio"]
        for Linea in Lectura:
            try:
                if len(Linea) == len(Cabecera):
                    OtroDicionario = dict(zip(Cabecera,Linea))
                    Precios[OtroDicionario["nombre"]] = OtroDicionario["precio"]
            except IndexError:
                print("### Se omitieron algunas filas con datos faltantes ###")
    return(Precios)
#--------------------------------------------------------------------
# %%
#
import csv
from pprint import pprint
pprint(leer_precios())
# %%
