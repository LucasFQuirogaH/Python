"""------------------------------------------------------------------------------------------------------------
Busqueda Binaria.
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%



# Funciones ---------------------------------------------------------------------------------------------------
## FUNCIONES FUNCION BUSQUEDA BINARIA -------------------------------------------------------------------------
# %%
def busqueda_binaria(lista, x, verbose = False):
    # Búsqueda binaria
    # Precondición: la lista está ordenada
    # Devuelve -1 si x no está en lista;
    # Devuelve p tal que lista[p] == x, si x está en lista
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    Contador = 0
    while izq <= der:
        Contador += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos , Contador

## FUNCIONES FUNCION DONDE INSERTAR ---------------------------------------------------------------------------
# %%
def donde_insertar(lista, x, verbose = False):
    # Funcion que devuelve el valor de la posiscion, si se encontro el elemento -------------------------------
    # sino no se encontro devuelve la posicion donde deberia ir. ----------------------------------------------
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1
    izq = 0
    der = len(lista) - 1
    Encontrado = False
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            Encontrado = True
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if Encontrado:
        return pos , True
    else:
        return izq , False

## FUNCIONES FUNCION 1 BUSQUEDA LINEAL ------------------------------------------------------------------------
# %%
def insertar(lista, x):
# Recibe una lista ordenada y un elemento. Si el elemento se encuentra en la lista solamente devuelve su ------
# posición; si no se encuentra en la lista, lo inserta en la posición correcta para mantener el orden. --------
# En este segundo caso, también debe devolver su posición. ----------------------------------------------------
    print(f'[DEBUG] izq |der |medio')
    pos = -1
    izq = 0
    der = len(lista) - 1
    Encontrado = False
    while izq <= der:
        medio = (izq + der) // 2
        print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            Encontrado = True
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if Encontrado:
        return pos , True , lista
    else:
        lista.insert( izq , x)
        return izq , False , lista

## FUNCIONES FUNCION PLAY QUE INICIA --------------------------------------------------------------------------
# %%
def play(lista , x):
# Inicia todo -------------------------------------------------------------------------------------------------
    posicion , Encontrado , lista = insertar(lista , x)
    if Encontrado:
        print(f"Se encuentra en la posicion {posicion}")
    else:
        print(f"No se encuentra, pero se colocó en la posicion {posicion}")
        print(lista)
    return None

# Main  --------------------------------------------------------------------------------------------------------
# %%
play([0 , 1 , 3 , 5 , 7 , 9] , 15 )

# %%
