"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
#
class Punto:
    def __init__(self , x , y):
        self.x = x
        self.y = y
# Metodos
    def __add__(self, b):
        return (self.x + b.x , self.y + b.y)
#--------------------------------------------------------------------
a = Punto(1 , 2)
b = Punto(3 , 5)
#--------------------------------------------------------------------
repr(a + b)
#--------------------------------------------------------------------
# %%
#

"""
a + b       a.__add__(b)
a - b       a.__sub__(b)
a * b       a.__mul__(b)
a / b       a.__truediv__(b)
a // b      a.__floordiv__(b)
a % b       a.__mod__(b)
a << b      a.__lshift__(b)
a >> b      a.__rshift__(b)
a & b       a.__and__(b)
a | b       a.__or__(b)
a ^ b       a.__xor__(b)
a ** b      a.__pow__(b)
-a          a.__neg__()
~a          a.__invert__()
abs(a)      a.__abs__()

Los siguientes métodos se usan para implementar contenedores:
len(x)      x.__len__()
x[a]        x.__getitem__(a)
x[a] = v    x.__setitem__(a,v)
del x[a]    x.__delitem__(a)

"""
# %%
"""
getattr(obj, 'name')          # Equivale a obj.name
setattr(obj, 'name', value)   # Equivale a obj.name = value
delattr(obj, 'name')          # Equivale a del obj.name
hasattr(obj, 'name')          # Mira si la propiedad existe
Ejemplo:

if hasattr(obj, 'x'):
    x = getattr(obj, 'x'):
else:
    x = None
Nota: si getattr() no encuentra el atributo buscado (x en este ejemplo),
devuelve el argumento opcional arg (None en este caso)

x = getattr(obj, 'x', None)
"""
#--------------------------------------------------------------------
# %%
#
import lote
c = lote.Lote('Peras', 100, 490.1)
columnas = ['nombre', 'cajones']
for colname in columnas:
    print(colname, '=', getattr(c, colname))

# %%
