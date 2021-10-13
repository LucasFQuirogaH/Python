# caddena = []
# espacios = 0
# cadena = ("1 3 8 4 2 6")
# todos = len(cadena)

# for c in cadena:
#     if c.isspace() :
#         espacios += 1

# rango = todos - espacios
# print(rango)


# for indice in range (6) :
#     caddena.append (int(cadena.split(" ")[indice]))
# print(caddena)
# caddena.sort()
# print(f"El menor es: {caddena[0]}")
# print(f"El mayor es: {caddena[5]}")



"""--------------------------------------------------------------------------------------------------------------------
Mensage enviado:
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest
number.
Example:
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
--------------------------------------------------------------------------------------------------------------------"""

"""--------------------------------------------------------------------------------------------------------------------
Funcion que recorre la lista o arreglo, y leugo muestra la cantidad de elementos consecutivos
--------------------------------------------------------------------------------------------------------------------"""
#Funciones
#recorro
def high_and_low(cadena):
    caddena = []
    c = 0
    espacios = 0
    rango = 0
   
    for c in cadena:
        if c.isspace() :
            espacios += 1

    rango = len(cadena) - espacios
  
    for indice in range (rango) :
        caddena.append (int(cadena.split(" ")[indice]))
    
    caddena.sort()
    return (caddena[0], caddena[rango - 1] )



"""--------------------------------------------------------------------------------------------------------------------
Main que pide al usuario la cantidad de datos a agregar a una lista donde se van a comparar luego.
--------------------------------------------------------------------------------------------------------------------"""
   
#Main
lista=("")
cadena = input ("Ingrese la cadena de numeros: ")

print (high_and_low (cadena))

