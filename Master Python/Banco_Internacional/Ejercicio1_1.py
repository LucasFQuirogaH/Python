# Your task is to find the first element of an array that is not consecutive.
# By not consecutive we mean not exactly 1 larger than the previous element of the array.
# E.g. If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive 
# but 6 is not, so that's the first non-consecutive number.


"""--------------------------------------------------------------------------------------------------------------------
Funcion que recorre la lista o arreglo, y leugo muestra la cantidad de elementos consecutivos
--------------------------------------------------------------------------------------------------------------------"""
#Funciones
#recorro
def NonConsecutive(lista, rango):
    contador = 0
    indice = 0
    NoConsecutivo = 0
    for indice in lista:
        if rango == 1:
            NoConsecutivo = "None"       
            break
        if (contador + 1) <= (rango - 1):
            if (lista [contador + 1]) != (indice + 1) :
                NoConsecutivo = lista [contador + 1]
                break
        else :
            break
        contador += 1
    if NoConsecutivo == 0 :
        NoConsecutivo = "None" 
    return (NoConsecutivo)


"""--------------------------------------------------------------------------------------------------------------------
Main que pide al usuario la cantidad de datos a agregar a una lista donde se van a comparar luego.
--------------------------------------------------------------------------------------------------------------------"""
   
#Main
lista=[]
rango = int(input ("Ingrese la cantidad de numeros que quiere almacenar en la lista: "))
for indice in range (rango) :
    lista.append (int(input ("Ingrese un nuevo numero: ")))

print(NonConsecutive(lista, rango))

