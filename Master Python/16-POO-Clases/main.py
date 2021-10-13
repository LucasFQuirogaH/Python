"""---------------------------------------------------------------------------------------------------------------------
Vamos a programar creando clases en progamacion orientada a objeto
---------------------------------------------------------------------------------------------------------------------"""





"""---------------------------------------------------------------------------------------------------------------------
Definicion de la clase
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
    
    
    # Velocidades
    def setVelocidad(self, nuevaVelocidad):
        self.velocidad = nuevaVelocidad
    
    def getVelocidad(self):
        return self.velocidad
    
"""---------------------------------------------------------------------------------------------------------------------
Crear o instanciar un objeto
---------------------------------------------------------------------------------------------------------------------"""
# Auto Comun
print("Del coche comun----------------------------------------------------------------------------------------")
auto = coche()
print("Su color por defecto es: " , auto.getColor())
auto.setColor("Verde")
print("Su nuevo color es: " , auto.getColor())

# Utilitario
print("Del Utilitario----------------------------------------------------------------------------------------")
utilitario = coche()
print("Su color por defecto es: " , utilitario.getColor())
utilitario.setColor("Gris")
print("Su nuevo color es: " , utilitario.getColor())
print("Su velocidad por defecto es: " , utilitario.getVelocidad())


