#Herencia -----------------------------------------------------------------------------------------------------
class Empleado:
    def __init__(self, nombre, edad , legajo , sueldo):
        self.edad = edad
        self.legajo = legajo
        self.sueldo = sueldo
        self.sueldoBase = sueldo

    def calcularSueldo(self , descuentos , bonos):
        return self.sueldoBase - descuentos + bonos
#--------------------------------------------------------------------------------------------------------------
class AgenteDeVentas(Empleado):
    def __init__(self, nombre, edad , legajo , sueldo , mostrador):
        super().__init__(nombre, edad , legajo , sueldo)
        self.mostrador = mostrador
#--------------------------------------------------------------------------------------------------------------
class Tripulante(Empleado):
    def mostarRenovacionLicencia(self):
        if self.edad < 50:
            print("Renueva su lincencia cada 1 año")
        else:
            print("Re nueva su licencia cada 6 meses")
#Ocultamiento y getters y setters -----------------------------------------------------------------------------
class Materia:
    def __init__(self, nombre , profesor , fecha):
        self.nombre = nombre
        self.profesor = profesor
        self.fechaInicioDictado = fecha

@property #Getter
def fechaInicioDictado (self):
    return self._fechaInicioDictado

@fechaInicioDictado.setter #Setter
def fechaInicioDictado(self , fecha):
    if fecha < 2006:
        self._fechaInicioDictado = 2006
    else:
        self._fechaInicioDictado = fecha