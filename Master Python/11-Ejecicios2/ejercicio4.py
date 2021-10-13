"""--------------------------------------------------------------------------------------------------------------------
Crear un scrip que tenga 4 variables, una lista, string, entero y un booleano.
Imprima un mensaje segun el tipo de dato de cada variable
-------------------------------------------------------------------------------------------------------------------"""



#Funciones-------------------------------------------------------------------------------------------------------------

def eltipo(dato):
    if isinstance (dato, list):
        print(f"La variable lista es del tipo: {type(dato)}")
    elif isinstance(dato, str):
        print(f"La variable string es del tipo: {type(dato)}")
    elif isinstance(dato, bool):
        print(f"La variable buleano es del tipo: {type(dato)}")
    elif isinstance(dato, int):
        print(f"La variable entero es del tipo: {type(dato)}")

    
        
       

#Main------------------------------------------------------------------------------------------------------------------

lista = ["soy el rey del mundo" , 16 , True]
string = "retrocer nunca rendirse jamas"
entero = 1998
buleano = False

eltipo(lista)
eltipo(string)
eltipo(entero)
eltipo(buleano)