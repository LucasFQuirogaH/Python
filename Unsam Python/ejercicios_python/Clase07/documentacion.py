"""------------------------------------------------------------------------------------------------------------
Ejercicio 7.8: Funciones y documentación
Ing.Lucas F. Quiroga H. Fecha: 28/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%


# Funciones ---------------------------------------------------------------------------------------------------
# Funciones: Valor Absoluto ----------------------------------------------------------------------------------
# %%
def valor_absoluto(n):
# Calculo del valor absoluto.Se debe administrar un valor numero real a la funcion, ya sea negativo o positivo.
# Luego, esta devolvera su valor en postivo, sin signo.
# Precondicion, un numero cualquiera.
# Poscondicion, el mismo numero pero siempre en positivo
    if n >= 0:
        return n
    else:
        return -n

# Funciones: Suma Pares -------------------------------------------------------------------------------------
# %%
def suma_pares(l):
# Sumador de elementos pares de una lista. Se le debe administrar una lista de elementos a esta funcion,
# para que luego devuelva el resultado de la sumatoria de los elementos seleccionados como pares.
# Precondicion: Una lista.
# Poscondicion: Un resultado producto de la suma de elementos seleccionados.
    res = 0
    for e in l:
        if e % 2 == 0:
            res += e
        else:
            res += 0
    return res
# Aqui el invariante es res, conteniendo la porcion de la sumatoria que se debe entregar al final
# de la funcion

# Funciones: Veces ------------------------------------------------------------------------------------------
# %%
def veces(a, b):
# Funcion multiplicadora. Se le debe administar 2 valores. El primero es el multiplicando.
# El segundo, el multiplicador.
# Precondicion: 2 valores, el multiplicando y el multiplicador.
# Poscondicion: Un resultado producto de la suma del multiplicando, tantas veces como lo especifica
# el multiplicador.
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
# Aqui el invariante es res, conteniendo la porcion de la sumatoria que se debe entregar al final
# de la funcion

# Funciones: Collatz ----------------------------------------------------------------------------------------
# %%
def collatz(n):
# Funcion collatz. Toma el valor n y lo lo divide por 2 si es par, o multiplica por 3 y suma 1, si es impar.
# Realiza iteraciones hasta que se llega al valor unitario. Todo este proceso ocurre, siempre y
# cuando el valor suministrado sea diferente al valor de destino.
# Precondicion: Asignacion de un numero real.
# Poscondicion: El resultado como el numero de iteraciones realizadas para llegar al valor 1.
    res = 1
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
    return res
# Aqui el invariante es res con la cantidad de iteraciones hasta el momento, mientras se ejecuta el ciclo.
# Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    return None


# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()
