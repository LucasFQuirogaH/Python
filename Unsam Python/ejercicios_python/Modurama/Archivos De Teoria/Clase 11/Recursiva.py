"""------------------------------------------------------------------------------------------------------------
Funciones recursivas
Ing.Lucas F. Quiroga H. Fecha: 12/06/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------------------------------------------------
# F u n c i o n   r e c u r s i v a   f a c t o r i a l
# Se defina un caso base (en este caso la indicación no recursiva de cómo calcular factorial(1)).
# Que el argumento de la función respete la precondición de que n debe ser un entero mayor o igual que 1.
#--------------------------------------------------------------------------------------------------------------
# %%
#
def factorial(n):
# Precondición: n entero positivo
# Devuelve: n!
    if n == 1:
        return 1
    return n * factorial(n - 1)
#--------------------------------------------------------------------
# Prueba de factorial
factorial(6)
#--------------------------------------------------------------------
# %%
#--------------------------------------------------------------------------------------------------------------
# A L G O R I T M O S   R E C U R S I V O    E   I T E R A T I V O
# Llamaremos algoritmos recursivos a aquellos que realizan llamadas recursivas para llegar al resultado, y
# algoritmos iterativos a aquellos que llegan a un resultado a través de una iteración mediante un ciclo
# definido o indefinido.
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
# Iterativo
def factorial(n):
# Precondición: n entero positivo
# Devuelve: n!
    fact = 1
    for num in range(n, 1, -1):
        fact *= num
    return fact
#--------------------------------------------------------------------------------------------------------------
# Prueba de factorial
factorial(6)
#--------------------------------------------------------------------------------------------------------------
"""------------------------------------------------------------------------------------------------------------
Otro
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
#
def potencia(b,n):
# Precondición: n >= 0
# Devuelve: b^n.
    if n <= 0:
        # caso base
        return 1
    if n % 2 == 0:
        # caso n par
        p = potencia(b, n // 2)
        return p * p
    else:
        # caso n impar
        p = potencia(b, (n - 1) // 2)
        return p * p * b
#--------------------------------------------------------------------
# Llamo a potencia
potencia (2 , 10)

# %%
#--------------------------------------------------------------------------------------------------------------
# F U N C I O N E S   W R A P P E R
# Cuando la funcion recursiva que necesita calcular un valor. Es necesario que debe colocar una funcion auxiliar
# que haga el trabajo y devuelva el valor que debe calcular.
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------
def promediar(lista):
# Devuelve el promedio de los elementos de una lista de números.
    def promediar_aux(lista):
        suma = lista[0]
        cantidad = 1
        if len(lista) > 1:
            suma_resto, cantidad_resto = promediar_aux(lista[1:])
            suma += suma_resto
            cantidad += cantidad_resto
        return suma, cantidad
    suma, cantidad = promediar_aux(lista)
    return suma / cantidad