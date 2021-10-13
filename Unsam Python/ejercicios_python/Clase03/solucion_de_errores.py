"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 3.1: Semántica
¿Anda bien en todos los casos de prueba?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
#----------------------------------------------------------------------------------------------------------------------------
# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n:
#         #if expresion[i] == 'a': 
#         #Comentario: El error era que no considera la mayuscula.
#         #Lo corregí agregando un or con la mayuscula correspondiente.
#         #A continuación va el código corregido
#         if (expresion[i] == 'a') or (expresion[i] == 'A'):
        
#         # if expresion[i] == 'a':
#         #     return True
#         # else:
#         #     return False
#         #Comentario: El error era la existencia de un if para return-ear.
#         #Lo corregí cambiando por una bandera donde estara el valor sea cual sea.
#         #A continuación va el código corregido. Se colcoa un break para que al encontrar al menos
#         #una A salga de todo bucle y return-ee
#             bandera = True
#             break
        
#         #i += 1
#         #Comentario: El error erala indentacion, i estaba dentro del bucle por lo que solo comparaba
#         #el primer caracter y lueo salia a return-ear
#         #Lo corregí indetando correctamente.
#         #A continuación va el código corregido
#         i += 1
#     return bandera



# print(tiene_a('UNSAM 2020'))
# print(tiene_a('abracadabra'))
# print(tiene_a('La novela 1984 de George Orwell'))

"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 3.2: Sintaxis
¿Anda bien en todos los casos de prueba?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

# #def tiene_a(expresion)
# #Comentario: El error era que no tenia los : al final de una definicion de funcion
# #Lo corregí colocando los :.
# #A continuación va el código corregido
# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     #while i<n
#     #Comentario: El error era que no tenia los : al final de la linea del while
#     #Lo corregí colocando los :.
#     #A continuación va el código corregido
#     while i<n:
#         #if expresion[i] = 'a'
#         #Comentario: El error era que no tenia los : al final de la linea del if y la comparacion se realiza con == en lugar de =.
#         #Lo corregí colocando los :.
#         #A continuación va el código corregido
#         if expresion[i] == 'a' or expresion[i] == 'A':
#             return True
#         i += 1
#     #return Falso
#     #Comentario: El error era falso en lugar de false.
#     #Lo corregí colocando false.
#     #A continuación va el código corregido
#         #return False
#         #Comentario: El error era la indentacion que hace salir de la funcion con un false en el primer caracter.
#         #Lo corregí indetnado correctamente.
#         #A continuación va el código corregido
#     return False
        

# print(tiene_a('UNSAM 2020'))
# print(tiene_a('La novela 1984 de George Orwell'))

"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 3.3: Tipos
¿Anda bien en todos los casos de prueba?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# def tiene_uno(expresion):
#     #Comentario: Se puede llegar a pasar a la funcion un dato que no sea string.
#     #Lo corregí casteando la expresion para cualquiera sea el caso:
#     #A continuación va el código corregido
#     expresion = str(expresion)
#     n = len(expresion)
#     i = 0
#     tiene = False
#     while (i<n) and not tiene:
#         if expresion[i] == '1':
#             tiene = True
#         i += 1
#     return tiene


# print(tiene_uno('UNSAM 2020'))
# print(tiene_uno('La novela 1984 de George Orwell'))
# print(tiene_uno(1984))
"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 3.4: Alcances
La siguiente suma no da lo que debería:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# def suma(a,b):
#     c = a + b
#     #Comentario: que return-ee un valor
#     #Lo corregí agregando un return
#     #A continuación va el código corregido
#     return c
# a = 2
# b = 3
# c = suma(a,b)
# print(f"La suma da {a} + {b} = {c}")

"""--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 3.5: Pisando memoria
El siguiente ejemplo usa el dataset de la clase anterior, pero no lo imprime como corresponde, ¿podés determinar por qué y explicarlo brevemente en la versión corregida?
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
            pass
            #El metodo append deja enganchado el valor del registro al camion, por lo que cualquier modificacion en las proximas iteraciones modificara los registros ya guardados.
            #Lo corregí agregando un reset al registro
            #A continuación va el código corregido
            registro = {}
    return camion

camion = leer_camion('Data/camion.csv')
pprint(camion)