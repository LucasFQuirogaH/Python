#--------------------------------------------------------------------
# %%
# 
class Empleado:
    def __init__(self, nombre, legajo , sueldo):
        self.nombre = nombre
        self.legajo = legajo
        self.sueldoBruto = sueldo
        
    def calcularSueldo(self , descuentos):
        return self.sueldoBruto - descuentos
#--------------------------------------------------------------------------------------------------------------
class Gerente(Empleado):
    def calcularSueldo(self, descuentos , bonificaciones):
        return self.sueldoBruto - descuentos + bonificaciones
    
#--------------------------------------------------------------------
# %%
# 
marcos = Empleado("Marcos Rios" , 221 , 30000)
julia = Gerente ("Julia Campos" , 109 , 60000)
# %%
