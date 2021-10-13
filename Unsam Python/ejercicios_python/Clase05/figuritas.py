"""----------------------------------------------------------------------------------------------------------------------------
5.9 El album de Figuritas
Implementá la función crear_album(figus_total) que devuelve un álbum (vector) vacío con figus_total espacios para pegar
figuritas.
----------------------------------------------------------------------------------------------------------------------------"""
# FUNCIONES -------------------------------------------------------------------------------------------------------------------
# FUNCION CREAR ALBUM --------------------------------------
# def crear_album(figus_total):
#     Album = np.zeros(figus_total , dtype = int)
#     return Album
# # MAIN -----------------------------------------------------
# import numpy as np
# import random
# N = 670
# AlbumDeFiguritas = crear_album(N)

"""----------------------------------------------------------------------------------------------------------------------------
Ejercicio 5.10: Incompleto
¿Cuál sería el comando de Python que nos dice si hay al menos un cero en el vector que representa el álbum? ¿Qué significa que
haya al menos un cero en nuestro vector?
Implemente la función album_incompleto(A) que recibe un vector y devuelve True si el vector contiene el elemento 0. En el caso
en que no haya ceros debe devolver False.
Estas funciones son tan sencillas --cada una puede escribirse en una sola línea-- que podría ponerse directamente esa línea
cada vez que queremos llamar a la función. Sin embargo, en esta etapa nos parece conveniente que organices el código en
funciones, por más que sean sencillas.
----------------------------------------------------------------------------------------------------------------------------"""
# FUNCIONES ----------------------------------------------------------------------------------------------------
# FUNCION CREAR ALBUM --------------------------------------
# def crear_album(figus_total):
#     Album = np.zeros(figus_total , dtype = int)
#     return Album
# # FUNCION ALBUM INCOMPLETO ---------------------------------
# def album_incompleto(AlbumDeFiguritas):
#     if 0 in AlbumDeFiguritas:
#         return True
#     else:
#         return False
# # MAIN --------------------------------------------------------------------------------------------------------
# import numpy as np
# import random
# N = 670
# AlbumDeFiguritas = crear_album(N)
# print(album_incompleto(AlbumDeFiguritas))

"""----------------------------------------------------------------------------------------------------------------------------
Ejercicio 5.11: Comprar
Alguna de las funciones que introdujimos en la Sección 5.1 sirve para devolver un número entero aleatorio dentro de un rango
(¿cuál era?). Implementá una función comprar_figu(figus_total) que reciba el número total de figuritas que tiene el álbum
(dado por el parámetro figus_total) y devuelva un número entero aleatorio que representa la figurita que nos tocó.
----------------------------------------------------------------------------------------------------------------------------"""
# FUNCIONES ----------------------------------------------------------------------------------------------------
# FUNCION CREAR ALBUM --------------------------------------
def crear_album(figus_total):
    Album = np.zeros(figus_total , dtype = int)
    return Album
# FUNCION ALBUM INCOMPLETO ---------------------------------
def album_incompleto(AlbumDeFiguritas):
    if 0 in AlbumDeFiguritas:
        return True
    else:
        return False
# FUNCION COMPRAR FIGU ---------------------------------
def comprar_figu(figus_total):
    return random.randint(0 , figus_total - 1)
# FUNCION COMPRAR FIGU ---------------------------------
def cuantas_figus(figus_total):
    AlbumNuevo = np.zeros(figus_total , dtype = int)
    while(album_incompleto(AlbumNuevo)):
        FiguritaComprada = comprar_figu(figus_total)
        AlbumNuevo[FiguritaComprada] += 1
    return AlbumNuevo
# FUNCION COMPRAR PAQUETE ------------------------------
def comprar_paquete(figus_total, figus_paquete):
    Figuritas = list(range(0 , figus_total))
    ListaDeFiguritas = random.sample(Figuritas , k = figus_paquete)
    return  np.array(ListaDeFiguritas)
# FUNCION CUANTOS PAQUETES -----------------------------
def cuantos_paquetes(figus_total, figus_paquete):
    AlbumNuevo = np.zeros(figus_total , dtype = int)
    CuentaPaquetes = 0
    Bandera = True
    while(album_incompleto(AlbumNuevo)):
        PaqueteComprado = comprar_paquete(figus_total, figus_paquete)
        CuentaPaquetes += 1
        for FiguritaNueva in PaqueteComprado:
            AlbumNuevo[FiguritaNueva] += 1
            if Bandera:
                if np.count_nonzero(AlbumNuevo) >= (0.9 * figus_total):
                    Contador90 = CuentaPaquetes
                    Bandera = False
    return CuentaPaquetes , Contador90

# FUNCIONES SOLIDARIAS -------------------------------------------------
def AlbumIncompletoSolidario(ListaDeAlbumesSolidarios):
    for Album in ListaDeAlbumesSolidarios:
        if 0 in Album:
            return True
        else:
            return False
def CuantosPaquetesSolidarios(figus_total, figus_paquete):
    ListaDeAlbumesSolidarios = []
    for i in range (5):
        AlbumNuevoSolidario = np.zeros(figus_total , dtype = int)
        ListaDeAlbumesSolidarios.append(AlbumNuevoSolidario)
        
    CuentaPaquetesSolidario = 0

    while(AlbumIncompletoSolidario(ListaDeAlbumesSolidarios)):
        PaqueteCompradoSolidario = comprar_paquete(figus_total, figus_paquete)
        CuentaPaquetesSolidario += 1
        
        for FiguritaNueva in PaqueteCompradoSolidario:
            for i , Album in enumerate(ListaDeAlbumesSolidarios):
                if Album[FiguritaNueva] == 0:
                    Album[FiguritaNueva] += 1
                    break #Rompe la busqueda de album
                elif i == 4:
                    Album[FiguritaNueva] += 1
    return CuentaPaquetesSolidario




"""---------------------------------------------------------------------------------------------------------"""
# MAIN --------------------------------------------------------------------------------------------------------
import numpy as np
import random
import pprint
import math
figus_total = 6

#5.9
AlbumDeFiguritas = crear_album(figus_total)

#5.10
# print(album_incompleto(AlbumDeFiguritas))


# 5.11
NumeroDeLaFigurita = comprar_figu(figus_total)
# print(AlbumDeFiguritas)

# 5.12
AlbumNuevo = cuantas_figus(figus_total)

# 5.13
# n_repeticiones = 1000
# UnaLista = []
# ResultadosObtenidos = []
# ConcatenoEste = []

# for i in range(n_repeticiones):
#     ConcatenoEste = cuantas_figus(figus_total)
#     ResultadosObtenidos = np.concatenate((ResultadosObtenidos , ConcatenoEste))
# print(f"En promedio, se necesitan comprar {np.mean(ResultadosObtenidos):0.2f} figuritas cada una para llenar el album de 6 Figuritas, con 1000 repeticiones")

#5.14
# n_repeticiones = 100
# figus_total = 670
# UnaLista = []
# ResultadosObtenidos = []
# ConcatenoEste = []

# for i in range(n_repeticiones):
#     ConcatenoEste = cuantas_figus(figus_total)
#     ResultadosObtenidos = np.concatenate((ResultadosObtenidos , ConcatenoEste))
# print(f"En promedio, se necesitan comprar {np.mean(ResultadosObtenidos):0.2f} figuritas cada una para llenar el album de 670 Figuritas, con 100 repeticiones")

"""---------------------------------------------------------------------------------------------------------------------------------
Ahora con paquetes
Estos ejercicios te recomendamos que los pienses y discutas con un compañere o alguna de tus otras personalidades (si es que tenés):
¿Cómo impacta en lo realizado tener paquetes con figuritas en lugar de figus sueltas? DE TENER POSIBILIDAD DE COMPRAR PAQUETES DE
FIGURITAS SEGURAMENTE OCUPARIA MENOS ITERACIONES PERO AUMENTARIA LAS FIGURITAS REPETIDAS
¿Cómo puede representarse un paquete? DEFINIMOS UN PAQUETE DE N FIGURITAS, Y GENERAR NUMEROS RANDOM DENTRO DEL PAQUETITO. LUEGO
REALIZO 2 FOR PARA LEER EL PAQUETITO Y AGREGAR UNA FIGURITA MAS AL ALBUM EN EL LUGAR QUE CORRESPONDA.
---------------------------------------------------------------------------------------------------------------------------------"""
#5.15

#5.16
figus_total = 670
figus_paquete = 5
# print(comprar_paquete(figus_total , figus_paquete))

#5.17
# Paquetitos , Contador90 = cuantos_paquetes(figus_total , figus_paquete)
# print(f"Se necesitan comprar {Paquetitos} paquetes para llenar el album")

#5.18
# n_repeticiones = 100
# figus_total = 670
# figus_paquete = 5
# ListaDeConcatenacion = []
# ListaDe90 = []
# Contador850 = 0

# for i in range(n_repeticiones):
#     Paquetitos , Contador90 = cuantos_paquetes(figus_total , figus_paquete)
#     if Paquetitos <= 850:
#         Contador850 +=1
#     ListaDeConcatenacion.append(Paquetitos)
#     ListaDe90.append(Contador90)
#     ResultadosObtenidos = np.array(ListaDeConcatenacion)
# print(f"En promedio, se necesitan comprar {np.mean(ResultadosObtenidos):0.2f} paquetes de figuritas cada una para llenar el album de 670 Figuritas, con 100 repeticiones")

#5.19
# print(f"La estimacion de la probabilidad es {(Contador850/n_repeticiones):0.2f}")

#5.20
# import matplotlib.pyplot as plt
# plt.hist(ResultadosObtenidos,bins=150)
# plt.ylabel("Ocurrencia")
# plt.xlabel("Cantidad de Paquetes")
# plt.show()

#5.21 0.29 da de probabilidad con comprar_paquete y random.choices(Figuritas , k = figus_paquete)
# print(f"El valor de la estimacion es de {np.mean(np.array(ListaDe90))} paquetes")

#5.22 0.37 da de probabilidad con comprar_paquete y random.sample(Figuritas , k = figus_paquete)

#5.23 PARA NO HACER LIO, ARME 3 FUNCIONES NUEVAS PARA TRABAJAR APARTE DE MANERA SOLIDARIA EN EL LLENADO DE LOS 5 ALBUMES.
ListaDeConteoDePaquetesSolidarios = []
for i in range(100):
    PaquetesSolidarios = CuantosPaquetesSolidarios(figus_total, figus_paquete)
    ListaDeConteoDePaquetesSolidarios.append(PaquetesSolidarios)
print(np.mean(np.array(ListaDeConteoDePaquetesSolidarios)))


#Estimado Profesor. Todos los ejercicios se encuentran operativos. Para realizar las pruebas correspondientes
# a cada punto, debe descomentar las lineas correspondientes para analizar. Saludos. LUCAS QUIROGA.-