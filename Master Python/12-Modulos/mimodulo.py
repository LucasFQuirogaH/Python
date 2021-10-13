#Modulo de Funciones---------------------------------------------------------------------------------------------------

def holamundo (nombre) :
    return f"Hola {nombre} como estais?"

def Calculadora (numero1 , numero2, basicas = False) :
    
    if basicas == True:
         
        cadena = f"La suma es {numero1 + numero2}"
        cadena += "\n"
        cadena += f"La resta es {numero1 - numero2}"
        cadena += "\n"
    else :
            
        cadena = f"La suma es {numero1 + numero2}"
        cadena += "\n"
        cadena += f"La resta es {numero1 - numero2}"
        cadena += "\n"
        cadena += f"La multiplicacion es {numero1 * numero2}"
        cadena += "\n"
        cadena += f"La division es {numero1 / numero2}"
        cadena += "\n"
        
    return (cadena)