# %% [markdown]
# # canguro_bueno.py
# ## Hecho por mi
# **Vamos!!!**
import copy
class Canguro:
    def __init__(self, Nombre, Cosas = []):
        self.nombre = Nombre
        self.ContenidosGuardados = Cosas.copy()
    def __str__(self):
        String = [self.nombre + " guarda en su bolsa: "]
        for Objeto in self.ContenidosGuardados:
            MasString = " " + object.__str__(Objeto)
            String.append(MasString)
        return str(",".join(String))

    def meter_en_marsupio(self, item):
        self.ContenidosGuardados.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
print()
print(cangurito)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.





#--------------------------------------------------------------------
# %%
# canguro_malo.py
"""Este código continene un
bug importante y dificil de ver
"""
import copy
class Canguro:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre, contenido = []):
        """Inicializar los contenidos del marsupio.
        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        # Realice una correccion del contenido desligando el contenido como una copia del original
        self.contenido_marsupio = contenido.copy()


    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """

        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)
print()
print(cangurito)
#
# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.
