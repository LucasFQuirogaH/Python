#--------------------------------------------------------------------
# %%
# 
from msilib.schema import Class

class punto():
    # Atributos ------------------------------------------------------------------------------------------------
    def __init__(self , x , y):
        self.x = x
        self.y = y
        
    # Metodos --------------------------------------------------------------------------------------------------
    def dist_origen(self):
        return (((self.x)**2 + (self.y)**2)**(0.5))
    
    def __str__(self):
        return f"{self.x} , {self.y}" # Aqui lo definis para hacer print
    
    def  __repr__(self):
        return f"Punto({self.x} , {self.y})" # Directamente llamas al punto como si estuvieras en una terminal
    
    
#--------------------------------------------------------------------------------------------------------------

# %%


# a.x
# a.y
# a.dist_origen
# print()
