# menor = int(input("Ingrese un numero cualquiera, entero obvio: "))
# mayor = int(input("Ingrese un numero cualquiera, mayor que el anterior: "))

# indice = menor + 1

# if (menor + 1) % 2 == 1:
#     renglon = str (menor + 1)
#     indice = menor + 2
# else:
#     renglon = str (menor + 2 )
#     indice = menor + 3

# while indice < mayor :
#     if indice % 2 == 1:
#         renglon = str (renglon) + " , " + str(indice)
#     indice += 1
# print(renglon)



menore = 0

menor = int(input("Ingrese un numero cualquiera, entero obvio: "))
mayor = int(input("Ingrese un numero cualquiera, mayor que el anterior: "))

if (menor + 1) % 2 == 1:
    renglon = str (menor + 1)
    menore = menor + 2
    
else:
    renglon = str (menor + 2 )
    menore = menor + 3


for indice in range (menore, mayor):
    if indice % 2 == 1 :
        renglon = str (renglon) + " , " + str(indice)

print(renglon)