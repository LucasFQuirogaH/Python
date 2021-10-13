# Hace un programa que tenga una lista de 8 numeros enteros.
# 1 -) Recorrer la lista y mostrarla en una funcion
# 2-) Ordenar y mostrarla
# 3- ) Mostar la longitud
# 4-) Buscar un elemento que le usuario pida

# Funcion recorro
def recorro(lista):
    contador = 0
    for indice in lista:
        contador += 1
        print(f"Elemento {contador} : {indice}")


def ordena(lista):
    lista.sort()
    print("\n Ordenada!")
    recorro(lista)


def busca(lista, rango):
   contador = 0
   indice = 0
   posicion = 0

   dato = int(input("Ingrese el dato a buscar: "))

   for indice in lista:
       if indice == dato:
            posicion = contador
            print(f"El dato esta en la posicion {posicion}")
            break
       if contador == (rango-1):
           print("El dato no esta en lista")
       contador += 1
    
# main
lista=[]
rango = int(input ("Ingrese la cantidad de numeros que quiere almacenar en la lista: "))
for indice in range (rango) :
    lista.append (int(input ("Ingrese un nuevo numero: ")))
    
recorro(lista)
ordena(lista)

print ("\n")
print (f"Su longitud es: {len(lista)}")

busca (lista, rango)
