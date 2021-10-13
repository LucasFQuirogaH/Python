"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 2.14: Diccionario geringoso.
Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso.
Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus traducciones al geringoso (como en el Ejercicio 1.18).
Probá tu función para la lista ['banana', 'manzana', 'mandarina']. Guardá este ejercicio en un archivo diccionario_geringoso.py para entregar al final de la clase.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Funciones ---------------------------------------------------------------------
def EnGeringoso(cadena):
    caddena = ""
    Diccionario_Geringoso = {}
    for linea in cadena:
        for c in linea:
            if c == "a":
                caddena = caddena + "apa"
            elif c == "e":
                caddena = caddena + "epe"
            elif c == "i":
                caddena = caddena + "ipi"
            elif c == "o":
                caddena = caddena + "opo"
            elif c == "u":
                caddena = caddena + "upu"
            else:
                caddena = caddena + c
        Diccionario_Geringoso[linea] = caddena
        caddena = ""
    print(Diccionario_Geringoso)

# Main -----------------------------------------------------------------------
cadena = ['banana', 'manzana', 'mandarina']
EnGeringoso(cadena)

