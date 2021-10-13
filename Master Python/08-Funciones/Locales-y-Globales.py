frase= "Retroceder nunca, rendirse jamas"

def holaMundo() :
    frase = "Hola Mundo"
    print (frase)
    
    global anio
    anio = 2021
    #print(anio)

holaMundo()
print(anio)
print(frase)