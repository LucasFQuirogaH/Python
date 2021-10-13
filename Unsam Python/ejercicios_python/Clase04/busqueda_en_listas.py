"""-----------------------------------------------------------------------------------------------
Ejercicio 4.6: Búsquedas de un elemento
Creá el archivo busqueda_en_listas.py para guardar tu código de este ejercicio y el siguiente.
En este primer ejercicio tenés que escribir una función buscar_u_elemento() que reciba una lista
y un elemento y devuelva la posición de la última aparición de ese elemento en la lista
(o -1 si el elemento no pertenece a la lista).
-----------------------------------------------------------------------------------------------"""
# FUNCIONES FUNCION 1 BUSQUEDA LINEAL --------------------------------------------------------
def BusquedaLineal(Lista, Buscado):
    Posicion = -1
    for indice , elemento in enumerate(Lista):
        if elemento == Buscado:
            Posicion = indice
            break
    return(Posicion)
# FUNCIONES FUNCION 2: BUSQUEDA Y CANTIDAD DE REPETICIONES -----------------------------------
def buscar_n_elemento(Lista, MasBuscado):
    Contando = 0
    for elemento in Lista:
        if elemento == Buscado:
            Contando += 1
    return(Contando)
# FUNCIONES FUNCION 3: BUSQUEDA DE UN MAXIMO -------------------------------------------------
def maximo(Lista):
    Maximo = -9999
    for elemento in Lista:
        if elemento > Maximo:
            Maximo = elemento
    return(Maximo)
# FUNCIONES FUNCION 4: BUSQUEDA DE UN MINIMO -------------------------------------------------
def minimo(Lista):
    Minimo = 0
    for elemento in Lista:
        if elemento < Minimo:
            Minimo = elemento
    return(Minimo)

# MAIN ---------------------------------------------------------------------------------------
Lista = [-5 , -4] #[1 , 3 , 5 , 7 , 9 , 1 , 3 , 3 , 3 , 65]
Buscado = int(input ("Ingrese el valor para buscar: "))
print((BusquedaLineal(Lista , Buscado)))
Cantidad = buscar_n_elemento(Lista, Buscado)
if Cantidad > 1:
    print(f"Se repite este mismo {Cantidad} veces")
ElMaximo = maximo(Lista)
print(f"El maximo es: {ElMaximo}")

ElMinimo = minimo(Lista)
print(f"El minimo es: {ElMinimo}")