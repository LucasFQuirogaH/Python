# contador = 0

# for contador in range (1 , 6) :
#     print("voy por " + str(contador))

multiplicador = int(input ("Ingrese el numero para mostrar su tabla de multiblicar: "))
indice = 0
for indice in range (1 , 10) :
    if multiplicador ==45:
        print("La tabla de ese numero no se puede mostar")
        break
    else :
        print (f"{multiplicador} x {indice} = {indice * multiplicador}")
else:
    print ("Fin de Tabla")