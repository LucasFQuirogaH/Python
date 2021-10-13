# frase= "Todos somos programadores"
# cadena = []
# contador = 0
# # caddena = ""
# for palabra in frase:
#     for letra in palabra:
#         cadena.append(letra)
# cadena.append(" ")
# # print(cadena)

# for letra in cadena:
#     if letra == " " :
#         if cadena[contador - 2 ] == "o":
#             cadena[contador - 2 ]= 'e'
#     contador +=1
# # caddena = "".join(cadena)

# print("".join(cadena))

"""-----------------------------------------------------------------------------------------------------------------------
Lenguaje Inclusivo
-----------------------------------------------------------------------------------------------------------------------"""
frase = ""
frase = input("Ingrese la frase: ")
cadena = []
contador = 0

for palabra in frase:
    for letra in palabra:
        cadena.append(letra)
cadena.append(" ")

for letra in cadena:
    if letra == " " :
        if (cadena[contador - 2 ] == "o") and (cadena[contador - 1] == "s") :
            cadena[contador - 2 ]= 'e'
    contador +=1
print("".join(cadena))