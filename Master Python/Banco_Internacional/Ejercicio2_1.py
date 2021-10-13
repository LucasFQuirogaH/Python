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
#high_and_low

def high_and_low(cadena):
    caddena = []
    temp = 0
    
    for c in cadena:
        if c.isdigit():
            temp = str(temp) + c
        elif c == "-" :
            temp = c
        elif c.isspace():
            caddena.append(int(temp))
            temp = 0
    caddena.append(int(temp))
    
    caddena.sort()
    return (caddena[0], caddena[(len(caddena)) - 1] )
    

"""--------------------------------------------------------------------------------------------------------------------
Main que pide al usuario la cantidad de datos a agregar a una lista donde se van a comparar luego.
--------------------------------------------------------------------------------------------------------------------"""
   
#Main
lista=("")
cadena = input ("Ingrese la cadena de numeros: ")

print (high_and_low (cadena))
