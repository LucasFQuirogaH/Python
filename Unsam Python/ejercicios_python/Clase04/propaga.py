"""--------------------------------------------------------------------------------------
Ejercicio 4.9: Propagación
Imaginate una fila con varios fósforos uno al lado del otro. Los fósforos pueden estar
en tres estados: nuevos, prendidos fuego o ya gastados (carbonizados). Representaremos
esta situación con una lista L con un elemento por fósforo, que en cada posición tiene
un 0 (nuevo), un 1 (encendido) o un -1 (carbonizado). El fuego se propaga inmediatamente
de un fósforo encendido a cualquier fósforo nuevo que tenga a su lado. Los fósforos
carbonizados no se encienden nuevamente.

Escribí una función llamada propagar que reciba un vector con 0's, 1's y -1's y devuelva
un vector en el que los 1's se propagaron a sus vecinos con 0. Guardalo en un archivo
propaga.py.
--------------------------------------------------------------------------------------"""
# FUNCIONES FUNCION 1: Propagacion ------------------------------------------------------
def propagar(Lista):
    ListaEncendida = Lista
    Bandera = True
    while (Bandera):
        for i in range(len(ListaEncendida)):
            if ListaEncendida[i] == 1:
                if (i + 1) != len(ListaEncendida) and ListaEncendida[i + 1] == 0:
                        ListaEncendida[i + 1] = 1
                if (i >= 1) and ListaEncendida[i - 1] == 0:
                    ListaEncendida[i - 1] = 1
                    Bandera = True
                    break
                else:
                    Bandera = False
    return ListaEncendida
# MAIN ----------------------------------------------------------------------------------
Lista = [ 0 , 0 , 1 , 0 , 0 , -1 , 1 , 0 , 1]
print("\n")
print(propagar(Lista))