# Your task is to find the first element of an array that is not consecutive.
# By not consecutive we mean not exactly 1 larger than the previous element of the array.
# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive 
# but 6 is not, so that's the first non-consecutive number.


"""--------------------------------------------------------------------------------------------------------------------
Funcion que recorre la lista o arreglo, y leugo muestra la cantidad de elementos consecutivos
--------------------------------------------------------------------------------------------------------------------"""
#Funciones
#recorro
def recorro(lista, rango):
    contador = 0
    indice = 0
    ListaConsecutivos = []
    for indice in lista:
        if contador == 0 :
            if (lista[contador + 1]) == (indice + 1) :
                ListaConsecutivos.append(lista[contador])
        elif contador == rango - 1 :
            if (lista[contador - 1] == indice - 1) :
                ListaConsecutivos.append(lista[contador])
        elif ((lista[contador + 1]) == indice + 1) and (lista[contador - 1] == indice - 1) :
            ListaConsecutivos.append(lista[contador])
            
        contador += 1
    print(ListaConsecutivos)



"""--------------------------------------------------------------------------------------------------------------------
Main que pide al usuario la cantidad de datos a agregar a una lista donde se van a comparar luego.
--------------------------------------------------------------------------------------------------------------------"""
   
#Main
lista=[]
rango = int(input ("Ingrese la cantidad de numeros que quiere almacenar en la lista: "))
for indice in range (rango) :
    lista.append (int(input ("Ingrese un nuevo numero: ")))

recorro(lista, rango)

