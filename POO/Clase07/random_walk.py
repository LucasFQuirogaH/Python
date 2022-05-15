"""------------------------------------------------------------------------------------------------------------
Ejercicio 7.10: Caminatas al azar
Se realiza una caminata al azar para realizar multiples ploteos.
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%
import numpy as np
import matplotlib.pyplot as plt

# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Random walk -------------------------------------------------------------------------------------
# %%
def randomwalk(largo):
# Contrato: Funcion que genera aleatoriamente puntos desde un minimo hasta un maximo con un largo sumistrado
# a la funcion.
# Precondicion: Se suministra un valor entero positivo.
# Poscondicion: Arreglo de N equivalente al valor suministrado entre los valores estipulados dentro de la
# funcion random.
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()

## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    N = 100000
    TodasLasCaminatas = []
    ElMaximo = -10000
    ElMinimo = 10000

    for i in range(12):
        Pasos = randomwalk(N)
        TodasLasCaminatas.append(Pasos)

    for i , Caminata in enumerate(TodasLasCaminatas):
        MaximoDeEstaCaminata = max(abs(Caminata))
        MinimoDeEstaCaminata = min(abs(Caminata))
        if MaximoDeEstaCaminata > ElMaximo:
            ElMaximo = MaximoDeEstaCaminata
            ElMaximoIndice = i
        if MinimoDeEstaCaminata < ElMinimo:
            ElMinimo = MinimoDeEstaCaminata
            ElMinimoIndice = i

    MasAlejada = TodasLasCaminatas[ElMaximoIndice]
    MenosAlejada = TodasLasCaminatas[ElMinimoIndice]

    fig = plt.figure()
    plt.subplot(2, 1, 1) # define la figura de arriba
    for Caminata in TodasLasCaminatas:
        plt.plot(Caminata) # dibuja la curva
    plt.xticks([]), plt.yticks([]) # saca las marcas
    plt.title("12 caminatas al azar")

    plt.subplot(2, 2, 3) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
    plt.plot(MasAlejada)
    plt.xticks([]), plt.yticks([])
    plt.title("La caminata mas alejada")

    plt.subplot(2, 2, 4) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
    plt.plot(MenosAlejada)
    plt.xticks([]), plt.yticks([])
    plt.title("La caminata menos alejada")

    plt.show()
    return None

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()

