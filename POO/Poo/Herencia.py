#--------------------------------------------------------------------
# %%
# 
class Empleado:
    def __init__(self, nombre, edad , legajo , sueldo):
        self.nombre = nombre
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
# %% [markdown]
# # Aqui las pruebas
# ## Retroceder Nunca, Rendirse Jamas..
# **Instrucciones**
pedro = AgenteDeVentas("Pedro Martinez" , 35 , "AR18551" , 400000 , "Principal")
Lucas = Tripulante("Lucas Quiroga" , 40 , "AR18551" , 400000)
# %%
