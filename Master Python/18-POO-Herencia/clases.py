"""--------------------------------------------------------------------------------------------------------------------
Herencia es la posibilidad de compartir atributos y metodos
entre las clases. Y que diferentes clases hereden de esta.
--------------------------------------------------------------------------------------------------------------------"""

class Persona:
    """Nombre
    Apellido
    Altura
    Edad"""
    
    
    #--------------GETTERS--------------
    def getNombre(self):
        return (self.nombre)
    def getApellido(self):
        return (self.Apellido)
    def getAltura(self):
        return (self.Altura)
    def getEdad(self):
        return (self.Edad)

    #--------------SETTERS--------------
    def setNombre(self , NuevoNombre):
        self.nombre = NuevoNombre
    def setApellido(self , NuevoApellido):
        self.Apellido = NuevoApellido
    def setAltura(self , NuevaAltura):
        self.Altura = NuevaAltura
    def setEdad(self , NuevaEdad):
        self.Edad = NuevaEdad

    #--------------OTRAS-------------------
    def Hablar(self):
        return ("Estoy hablando")
    def Caminar(self):
        return ("Estoy caminando")
    def Dormir(self):
        return ("Estoy durmiendo")
    
class Informatico(Persona):
    """Lenguajes
    Experiencia"""
    
    #Constructor--------------------------------------------------
    def __init__(self):   #!
        self.Lenguajes = "HTML , JAVASCRIP , CSS "              #!
        self.Experiencia = 5                                    #!
    # Fin del constructor ----------------------------------------
    
    #--------------SETTERS--------------
    def setLenguajes(self):
        return self.Lenguajes
    def Aprender(self , NuevoLenguaje):
        self.Lenguajes = NuevoLenguaje
    
    #--------------GETTERS-------------    
    def getLenguajes(self):
        return(self.Lenguajes)
    def getExperiencia(self):
        return(self.Experiencia)
    
        
    #--------------OTRAS----------------
    def Programar(self):
        return ("Estoy programando")
    def Reparar(self):
        return ("Estoy reparando")
    
class TecnicoDeRedes(Informatico):
    def __init__(self):
        self.AuditarRedes = 'Experto'
        self.ExperienciaEnRedes = 15
        
    def Auditoria(self):
        return("Estoy auditando una red")