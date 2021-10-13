#--------------------------------------------------------------------------------------------------------------
# Clase
class Lote:
    def __init__(self, nombre, cajones , precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
#--------------------------------------------------------------------
# Metodos
    def costo(self):
        costo = self.precio * self.cajones
        return (costo)
    def vender(self , cantidad):
        total = self.precio * cantidad
        return (total)
#--------------------------------------------------------------------
    def CostoInflado(self):
        return self.costo() * 1.5
#--------------------------------------------------------------------
# Metodo Especial para imprimir
    def __str__(self):
        return f'({self.nombre} , {self.cajones} , {self.precio})'
# Metodo Especial para imprimir mas para programadores
    def __repr__(self):
        return f'Fruta({self.nombre} , {self.cajones} , {self.precio})'
#--------------------------------------------------------------------------------------------------------------
# Herencia
class MiLote(Lote):
    def rematar(self):
        self.vender(self.cajones)
    def costo(self):
        return 1.25 * super().costo()
#--------------------------------------------------------------------------------------------------------------
# Desde el otro archivo lo llamas como
# formateador = formato_tabla.crear_formateador(fmt)
# imprimir_informe(data_informe , formateador)
def crear_formateador(nombre):
    if nombre == "txt":
        return FormatoTablaTXT()
    elif nombre == "csv":
        return FormatoTablaCSV()
    elif nombre == "html":
        return FormatoTablaHTML()
    else:
        raise SystemExit ("No se entiende el formato")
#--------------------------------------------------------------------