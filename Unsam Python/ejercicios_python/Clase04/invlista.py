"""-----------------------------------------------------------------------------------------------
Escribí una función invertir_lista(lista) que dada una lista devuelva otra que tenga
los mismos elementos pero en el orden inverso. Es decir, el que era el primer elemento
de la lista de entrada deberá ser el último de la lista de salida y análogamente con
los demás elementos.
-----------------------------------------------------------------------------------------------"""
# FUNCIONES FUNCION 1: Inversion de un lista -------------------------------------------------


def invertir_lista(Lista):
    invertida = list(range(len(Lista)))
    for indice, elemento in enumerate(Lista):
        invertida[len(Lista) - indice - 1] = elemento
    return invertida


# MAIN ---------------------------------------------------------------------------------------
Lista = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
print(invertir_lista(Lista))
