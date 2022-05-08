
"""-----------------------------------------------------------------------------------------------------------------------
Ejercicio 1.13: El volumen de una esfera
En tu directorio de trabajo de esta clase, escribí un programa llamado esfera.py que le pida al usuario que
ingrese por teclado el radio r de una esfera y calcule e imprima el volumen de la misma.
Sugerencia: recordar que el volúmen de una esfera es 4/3 πr^3.
-----------------------------------------------------------------------------------------------------------------------"""

#Main---------------------------------------------------------------------------------------------------------------------

from cmath import pi


radio = int(input("Ingrese el radio"))
print(f"El volumen es: {((4*pi*(radio)**3))/3}")