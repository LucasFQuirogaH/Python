"""-----------------------------------------------------------------------------------------------------------------------
Ejercicio 1.18: Geringoso rústico
Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu'
según corresponda luego de cada vocal.
---------------------------------------------------------------------------------------------------------------------"""
PalabraReformateada = ""
palabra = input("Ingrese la palabra: ")
for letra in palabra:
    if letra == 'a':
        PalabraReformateada += letra + 'pa'
    elif letra == 'e':
        PalabraReformateada += letra + 'pe'
    elif letra == 'e':
        PalabraReformateada += letra + 'pe'
    elif letra == 'i':
        PalabraReformateada += letra + 'pi'
    elif letra == 'o':
        PalabraReformateada += letra + 'po'
    elif letra == 'u':
        PalabraReformateada += letra + 'pu'
    else:
        PalabraReformateada += letra
print(PalabraReformateada)
