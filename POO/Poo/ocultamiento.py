#--------------------------------------------------------------------
# %%
# 
class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materias = []
    
    def agregar(self , codigo , materia):
        self.materias[codigo] = materia

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
# %%
ing = Carrera("Ingenieria")

#--------------------------------------------------------------------
# %%
# 
algebra = Materia("Algebra" , "Ricardo Quinteros", 2010)
fisica = Materia("Fisica" , "Margarita Gomez" , 2006)
quimica = Materia ("Quimica" , "Lorena Rios" , 2003)

#--------------------------------------------------------------------
# %%
# 
ing.materias.append(134 , algebra)
ing.materias.append(142 , fisica)

ing.materias
