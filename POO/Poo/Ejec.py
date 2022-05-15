#--------------------------------------------------------------------
# %%
# 
class Gato:
    
    especie = "mamifero" # Atributo de clase, atributo fijo
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.alimentos = [] # Al no colocarlo en los parametros podes rellenarlo despues
        
    def verEtapaDeVida(self):
        if self.edad > 1:
            print("Es mayor de edad")
        else:
            print("Es chiquito")
        
#     def costo(self):
#         costo = self.precio * self.cajones
#         return (costo)
#     def vender(self , cantidad):
#         total = self.precio * cantidad
#         return (total)
# # Metodo Especial para imprimir
#     def __str__(self):
#         return f'({self.nombre} , {self.cajones} , {self.precio})'
# # Metodo Especial para imprimir mas para programadores
#     def __repr__(self):
#         return f'Fruta({self.nombre} , {self.cajones} , {self.precio})'
#--------------------------------------------------------------------
# %%
# 
p = Gato("Pelusa" , 1)
p.cantidadDePatas = 4
# %%
