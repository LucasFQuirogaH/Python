"""-------------------------------------------------------------------------------------------------------------------------------------------
3.6 Arbolado porteño
En esta sección haremos algunos ejercicios que integran los conceptos aprendidos en las clases anteriores.
Vamos a manejar archivos, diccionarios, listas, contadores y el comando zip, entre otras cosas. Entregá lo que puedas hacer.
Ejercicios
Vamos a repasar las herramientas que vimos en esta clase aplicándolas a una base de datos sobre árboles en parques de la Ciudad de Buenos Aires.
Para empezar, descargá el archivo CSV de "Arbolado en espacios verdes" en tu carpeta Data. Vamos a estudiar esta base de datos
y responder algunas preguntas. Guardá los ejercicios de esta sección en un archivo arboles.py.
-------------------------------------------------------------------------------------------------------------------------------------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 3.18: Lectura de los árboles de un parque
Definí una función leer_parque(nombre_archivo, parque) que abra el archivo indicado y devuelva una lista de diccionarios
con la información del parque especificado. La función debe devolver, en una lista un diccionario con todos los datos por
cada árbol del parque elegido (recordá que cada fila del csv es un árbol).

Sugerencia: basate en la función leer_camion() y usá también el comando zip como hiciste en el Ejercicio 3.9 para combinar
el encabezado del archivo con los datos de cada fila. Inicialmente no te preocupes por los tipos de datos de cada columna,
pero cuando empieces a operar con una columna modificá esta función para que ese dato sea del tipo adecuado para operar.

Observación: La columna que indica el nombre del parque en el que se encuentra el árbol se llama 'espacio_ve' en el archivo CSV.

Probá con el parque "GENERAL PAZ" para tener un ejemplo de trabajo, debería darte una lista con 690 árboles.
-------------------------------------------------------------------------------------------------------------------------------------------"""
# def leer_parque(nombre_archivo , parque):
#     import csv
#     Nombre ="Data/" + nombre_archivo + ".csv"
#     ElParquePedido = []
#     global contador
#     contador = 0
# # -----------------------------------------------------INTENTAR
#     try:
#         with open(Nombre , "r" , encoding="utf8") as Creacion:
#             Lectura = csv.reader(Creacion)
#             cabecera = next(Lectura)
#             for Linea in Lectura:
#                 if Linea[10] == parque:             
#                     UnDiccionario = dict(zip(cabecera, Linea))
#                     ElParquePedido.append(UnDiccionario)
#                     UnDiccionario = {}
#                     contador += 1
# # ------------------------------------------------  EXCEPCIONES                
#     except ValueError:
#         print("Existe un problema con el archivo selecionado")
#     except FileNotFoundError:
#         print("El archivo no se encuentra en el directorio")
#     except IndexError:
#         print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
#     return (ElParquePedido)

# # MAIN --------------------------------------------------------------------------------------------------
# import pprint
# arboles = leer_parque("arbolado-en-espacios-verdes", "GENERAL PAZ")
# pprint.pprint(arboles)
# print(f"Cantidad de arboles seleccionados: {contador} arboles")





"""-------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 3.19: Determinar las especies en un parque.
Escribí una función especies(lista_arboles) que tome una lista de árboles como la generada en el ejercicio anterior
y devuelva el conjunto de especies (la columna 'nombre_com' del archivo) que figuran en la lista.

Sugerencia: Usá el comando set como en la Sección 2.4.
-------------------------------------------------------------------------------------------------------------------------------------------"""
# ################ FUNCIONES -------------------------------------------------------------------------------------------------------------------
# # UNA FUNCION --------------------------------------------------------------------------------------------------------------------------------
# def leer_parque(nombre_archivo , parque):
#     import csv
#     Nombre ="Data/" + nombre_archivo + ".csv"
#     ElParquePedido = []
#     global contador
#     contador = 0
#     try:
#         with open(Nombre , "r" , encoding="utf8") as Creacion:
#             Lectura = csv.reader(Creacion)
#             cabecera = next(Lectura)
#             for Linea in Lectura:
#                 if Linea[10] == parque:             
#                     UnDiccionario = dict(zip(cabecera, Linea))
#                     ElParquePedido.append(UnDiccionario)
#                     UnDiccionario = {}
#                     contador += 1            
#     except ValueError:
#         print("Existe un problema con el archivo selecionado")
#     except FileNotFoundError:
#         print("El archivo no se encuentra en el directorio")
#     except IndexError:
#         print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
#     return (ElParquePedido)

# # OTRA FUNCION -------------------------------------------------------------------------------------------------------------------------------
# def especies(lista_arboles):
#     import csv
#     ListaDeValores = []
#     ConjuntoDeEspecies = []
#     try:
#         for Linea in lista_arboles:
#             ListaDeValores = list(Linea.values())
#             ConjuntoDeEspecies.append(ListaDeValores[7])
#             ListaDeValores =[]
#     except ValueError:
#         print("Existe un problema con el archivo selecionado")
#     except FileNotFoundError:
#         print("El archivo no se encuentra en el directorio")
#     except IndexError:
#         print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
#     return (ConjuntoDeEspecies)

# # MAIN ---------------------------------------------------------------------------------------------------------------------------------------
# import pprint
# lista_arboles = leer_parque("arbolado-en-espacios-verdes", "GENERAL PAZ")
# ConjuntoDeEspecies = especies(lista_arboles)
# pprint.pprint(ConjuntoDeEspecies)



"""-------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 3.20: Contar ejemplares por especie
Usando contadores como en el Ejercicio 3.11, escribí una función contar_ejemplares(lista_arboles) que,
dada una lista como la que generada con leer_parque(), devuelva un diccionario en el que las especies
(recordá, es la columna 'nombre_com' del archivo) sean las claves y tengan como valores asociados
la cantidad de ejemplares en esa especie en la lista dada.

Luego, combiná esta función con leer_parque() y con el método most_common() para informar las
cinco especies más frecuentes en cada uno de los siguientes parques:

'GENERAL PAZ'
'ANDES, LOS'
'CENTENARIO'
-------------------------------------------------------------------------------------------------------------------------------------------"""
################ FUNCIONES -------------------------------------------------------------------------------------------------------------------
# # UNA FUNCION --------------------------------------------------------------------------------------------------------------------------------
# def leer_parque(nombre_archivo , parque):
#     import csv
#     Nombre ="Data/" + nombre_archivo + ".csv"
#     ElParquePedido = []
#     global contador
#     contador = 0
#     try:
#         with open(Nombre , "r" , encoding="utf8") as Creacion:
#             Lectura = csv.reader(Creacion)
#             cabecera = next(Lectura)
#             for Linea in Lectura:
#                 if Linea[10] == parque:             
#                     UnDiccionario = dict(zip(cabecera, Linea))
#                     ElParquePedido.append(UnDiccionario)
#                     UnDiccionario = {}
#                     contador += 1            
#     except ValueError:
#         print("Existe un problema con el archivo selecionado")
#     except FileNotFoundError:
#         print("El archivo no se encuentra en el directorio")
#     except IndexError:
#         print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
#     return (ElParquePedido)

# # OTRA FUNCION -------------------------------------------------------------------------------------------------------------------------------
# def especies(lista_arboles):
#     import csv
#     ListaDeValores = []
#     ConjuntoDeEspecies = []
#     try:
#         for Linea in lista_arboles:
#             ListaDeValores = list(Linea.values())
#             ConjuntoDeEspecies.append(ListaDeValores[7])
#             ListaDeValores =[]
#     except ValueError:
#         print("Existe un problema con el archivo selecionado")
#     except FileNotFoundError:
#         print("El archivo no se encuentra en el directorio")
#     except IndexError:
#         print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
#     return (ConjuntoDeEspecies)

# # OTRA FUNCION -------------------------------------------------------------------------------------------------------------------------------
# def contar_ejemplares(lista_arboles):
#     from collections import Counter
#     return(Counter(lista_arboles))
# # OTRA FUNCION -------------------------------------------------------------------------------------------------------------------------------
# def mas_comunes(ContandoEjemplares):
#     from collections import Counter
#     return(ContandoEjemplares.most_common(5))

# # MAIN ---------------------------------------------------------------------------------------------------------------------------------------
# import pprint
# lista_arboles = leer_parque("arbolado-en-espacios-verdes", "CENTENARIO")
# lista_arboles = especies(lista_arboles)
# # pprint.pprint(lista_arboles)
# ContandoEjemplares = contar_ejemplares(lista_arboles)
# # print(ContandoEjemplares)
# LosMasComunes = mas_comunes(ContandoEjemplares)
# print(LosMasComunes)

"""-------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 3.21: Alturas de una especie en una lista
Escribí una función obtener_alturas(lista_arboles, especie) que, dada una lista de árboles como la anterior
y una especie de árbol (un valor de la columna 'nombre_com' del archivo), devuelva una lista con las alturas
(columna 'altura_tot') de los ejemplares de esa especie en la lista.

Observación: Acá sí, fijate de devolver las alturas como números (de punto flotante) y no como cadenas de caracteres.
Podés hacer esto modificando leer_parque.

Usala para calcular la altura promedio y altura máxima de los 'Jacarandá' en los tres parques mencionados.
-------------------------------------------------------------------------------------------------------------------------------------------"""
################ FUNCIONES -------------------------------------------------------------------------------------------------------------------
# UNA FUNCION --------------------------------------------------------------------------------------------------------------------------------
def leer_parque(nombre_archivo , parque):
    import csv
    Nombre ="Data/" + nombre_archivo + ".csv"
    ElParquePedido = []
    global contador
    contador = 0
    try:
        with open(Nombre , "r" , encoding="utf8") as Creacion:
            Lectura = csv.reader(Creacion)
            next(Lectura)
            for Linea in Lectura:
                if Linea[10] == parque:
                    ElParquePedido.append(Linea)
                    contador += 1            
    except ValueError:
        print("Existe un problema con el archivo selecionado")
    except FileNotFoundError:
        print("El archivo no se encuentra en el directorio")
    except IndexError:
        print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
    return (ElParquePedido)

# OTRA FUNCION -------------------------------------------------------------------------------------------------------------------------------
def especies(lista_arboles):
    import csv
    ConjuntoDeEspecies = []
    try:
        for Linea in lista_arboles:
            ConjuntoDeEspecies.append(Linea[7])
    except ValueError:
        print("Existe un problema con el archivo selecionado")
    except FileNotFoundError:
        print("El archivo no se encuentra en el directorio")
    except IndexError:
        print("El archivo contiene columnas diferentes para poder realizar los calculos solicitados")
    return (ConjuntoDeEspecies)
# OTRA FUNCION -------------------------------------------------------------------------------------------------------------------------------
def contar_ejemplares(lista_arboles):
    from collections import Counter
    ListaParaConteo = []
    for Linea in lista_arboles:
        ListaParaConteo.append(Linea[7])
    return(Counter(ListaParaConteo))
# OTRA FUNCION -------------------------------------------------------------------------------------------------------------------------------
def mas_comunes(ContandoEjemplares):
    from collections import Counter
    return(ContandoEjemplares.most_common(5))
# OTRA FUNCION -------------------------------------------------------------------------------------------------------------------------------
def obtener_alturas(lista_arboles, especie):
    ListaDeAlturas = []
    for Linea in lista_arboles:
        if especie == Linea[7]:
            ListaDeAlturas.append(float(Linea[3]))
    return(ListaDeAlturas)
# OTRA FUNCION -------------------------------------------------------------------------------------------------------------------------------
def obtener_inclinaciones(lista_arboles, especie):
    ListaDeInclinaciones = []
    for Linea in lista_arboles:
        if especie == Linea[7]:
            ListaDeInclinaciones.append(float(Linea[5]))
    return(ListaDeInclinaciones)

def especimen_mas_inclinado(lista_arboles):
    EMI_ListaDeEspecies =[]
    EMI_ListaDeInclinaciones = []
    ListaDeMaximos = []
    indice = 0
    
    # 1 Obtener la lista de especies
    EMI_ListaDeEspecies = especies(lista_arboles)
    # 2 Obtener una lista de inclinaciones
    for CadaEspecie in EMI_ListaDeEspecies:
        EMI_ListaDeInclinaciones = obtener_inclinaciones(lista_arboles, CadaEspecie)
        # 3 Obtenes el maximo de inclinacion para esa especie
        ListaDeMaximos.append(max(EMI_ListaDeInclinaciones))

    MaximoAnterior = 0.0
    for i , EsteEs in enumerate(ListaDeMaximos):
        if EsteEs > MaximoAnterior:
            MaximoAnterior = EsteEs
            indice = i
    
    print(f"La maxima inclinacion es de {ListaDeMaximos[indice]} que corresponde a la especie {EMI_ListaDeEspecies[indice]}")

def especie_promedio_mas_inclinada(lista_arboles):
    EPMI_ListaDeEspecies =[]
    EPMI_ListaDeInclinaciones = []
    ListaDePromediosMaximos = []
    indice = 0
    
    EPMI_ListaDeEspecies = especies(lista_arboles)
    for CadaEspecie in EPMI_ListaDeEspecies:
        EPMI_ListaDeInclinaciones = obtener_inclinaciones(lista_arboles, CadaEspecie)
        ListaDePromediosMaximos.append(mean(EPMI_ListaDeInclinaciones))

    MaximoPromedioAnterior = 0.0
    for i , EsteEs in enumerate(ListaDePromediosMaximos):
        if EsteEs > MaximoPromedioAnterior:
            MaximoPromedioAnterior = EsteEs
            indice = i

    print(f"La maxima inclinacion promedio es de {ListaDePromediosMaximos[indice]} que corresponde a la especie {EPMI_ListaDeEspecies[indice]}")

# MAIN ---------------------------------------------------------------------------------------------------------------------------------------
import pprint
from statistics import mean
promedio = 0.0
# 3.18
parque = "CENTENARIO"
lista_arboles = leer_parque("arbolado-en-espacios-verdes", parque)
pprint.pprint(lista_arboles)
# 3.19
Especies = especies(lista_arboles)
print("\n")
print("Lista de especies:")
pprint.pprint(Especies)
# 3.20
ContandoEjemplares = contar_ejemplares(lista_arboles)
print("\n")
print("Contador de Ejemplares:")
pprint.pprint(ContandoEjemplares)
LosMasComunes = mas_comunes(ContandoEjemplares)
print("\n")
print("Lista de ejemplares mas comunes:")
pprint.pprint(LosMasComunes)
# 3.21
especie =  "Jacarandá"
Alturas = obtener_alturas(lista_arboles, especie)
print("\n")
print(f"Lista de alturas de {especie} en parque {parque}:")
pprint.pprint(Alturas)

promedio = mean(Alturas)
AlturaMaxima = max(Alturas)
print("\n")
print(f"El promedio de {especie} es : {promedio:0.2f}")
print(f"La altura maxima de {especie} es : {AlturaMaxima}")

# 3.22
Inclinaciones = obtener_inclinaciones(lista_arboles, especie)
print("\n")
print(f"Lista de inclinaciones de {especie} en parque {parque}:")
pprint.pprint(Inclinaciones)

# 3.23
print("\n")
especimen_mas_inclinado(lista_arboles)

# 3.24
print("\n")
especie_promedio_mas_inclinada(lista_arboles)