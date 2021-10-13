# indice = 1
# renglon = str(0)
# for indice in range (1 , 120) :
#     if (indice % 2 == 0) :
#        renglon = renglon + " , " + str(indice)
#     indice += 1
# print(renglon)

indice = 1
renglon = str(0)
for indice in range (1 , 120) :
    if (indice % 2 == 0) :
       print(f"{indice} es par")
    else:
        print(f"{indice} es impar")
    indice += 1
