"""---------------------------------------------------------------------------------------------------------------------
Definicion de la clase COCHE
---------------------------------------------------------------------------------------------------------------------"""

class coche:
    #Atributos----------------------------------------------------------------------------------------------------------
    color = "Rojo"
    modelo = "Ferrari"
    velocidad = 300

    #Metodos------------------------------------------------------------------------------------------------------------
    
    # Colores
    def setColor(self, nuevoColor):
        self.color = nuevoColor
    
    def getColor(self):
        return self.color
    
    # Modelos
    def setModelo(self, nuevoModelo):
        self.modelo = nuevoModelo
    
    def getModelo(self):
        return self.modelo
    
     # Velocidad
    def setVelocidad(self, nuevaVelocidad):
        self.velocidad = nuevaVelocidad
    
    def getVelocidad(self):
        return self.velocidad
    
    
    # Informacion TOTAL
    def getTotal (self) :
        return ("Informacion total:\n" + "Su color es: " + self.getColor() + "\n" + "Su modelo es: " + self.getModelo() + "\n" + "Su maxima velocidad es: " + str (self.getVelocidad()))

    
    # Velocidades
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

        
    #Constructor--------------------------------------------------
    
    def __init__(self, colorinit, modeloinit, velocidadinit):   #!
        self.color = colorinit                                  #!
        self.modelo = modeloinit                                #!
        self.velocidad = velocidadinit                          #!
        
    # Fin del constructor ----------------------------------------