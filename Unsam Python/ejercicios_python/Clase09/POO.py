#--------------------------------------------------------------------
# %%
# Definicion de la clase
class Jugador:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.salud = 100
#--------------------------------------------------------------------
# class Jugador:
#     x = 2
#     y = 6
#     salud = 100
#--------------------------------------------------------------------
# Definicion del metodo
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def lastimar(self, pts):
        self.salud -= pts
#--------------------------------------------------------------------
# Getter y Setter x
    def setx(self , x):
        self.x = x
    def getx(self):
        return self.x
#--------------------------------------------------------------------
# Getter y Setter y
    def sety(self , y):
        self.y = y
    def gety(self):
        return self.y
#--------------------------------------------------------------------
# Getter y Setter x
    def setSalud(self , pts):
        self.lastima(pts)
    def getSalud(self):
        return self.salud
#--------------------------------------------------------------------------------------------------------------
# %%
# Crear un objeto mediante el llamado a la clase como si fuera
# una funcion
a = Jugador(2, 3)
#--------------------------------------------------------------------
# %%
a.x
#--------------------------------------------------------------------
# %%
#
a.y
# %%
a.getx()
# %%
a.setx(6)
# %%
