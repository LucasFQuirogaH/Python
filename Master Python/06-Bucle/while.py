# contador = 1
# while contador <= 10 :
#     print (f"Estoy en el numero {contador}")
#     contador += 1

# contador = 1
# renglon = str (0)

# while contador <= 10 :
#     renglon = renglon + "," + str(contador)
#     contador += 1
# print(renglon)

indice = 1
multiplicador = int (input("Ingrese el numero de la tabla que necesita: "))
while indice <= 10:
    print(f"{multiplicador} x {indice} = {multiplicador*indice}")
    indice += 1
else :
    print("Tabla Terminada")
