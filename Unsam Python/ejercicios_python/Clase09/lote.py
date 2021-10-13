#--------------------------------------------------------------------
# %%
#
class Lote:
    def __init__(self, nombre, cajones , precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    def costo(self):
        costo = self.precio * self.cajones
        return (costo)
    def vender(self , cantidad):
        total = self.precio * cantidad
        return (total)

def __repr__(self):
    return f"Lote({self.nombre} , {self.cajones} , {self.precio})"
