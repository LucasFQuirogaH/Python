menor = int(input("Ingrese un numero cualquiera, entero obvio: "))
mayor = int(input("Ingrese un numero cualquiera, mayor que el anterior: "))

indice = menor + 2
renglon = str(menor + 1)

while indice > (menor + 1) and indice < mayor :
    renglon = renglon + " , " + str(indice)
    indice += 1
print(renglon)