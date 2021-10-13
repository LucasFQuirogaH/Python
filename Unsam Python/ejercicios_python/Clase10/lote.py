#--------------------------------------------------------------------
# %%
#
class Lote:
    def __init__(self, nombre, cajones , precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def __repr__(self):
        return f'Lote({self.nombre} , {self.cajones} , {self.precio})'
    def __str__(self):
        return f'({self.nombre},{self.cajones},{self.precio})'

    def costo(self):
        costo = self.precio * self.cajones
        return (costo)
    def vender(self , cantidad):
        total = self.precio * cantidad
        return (total)

