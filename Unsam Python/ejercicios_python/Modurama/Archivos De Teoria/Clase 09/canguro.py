#--------------------------------------------------------------------
# %%
#
class Canguro:
    def __init__(self, nombre, contenido):
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        self.contenido_marsupio.append(item)
#--------------------------------------------------------------------
madre_canguro = Canguro('Madre' , [])
cangurito = Canguro('gurito' , [])
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)
#--------------------------------------------------------------------
# %%
#
print(madre_canguro)
#--------------------------------------------------------------------
# %%
#
print(cangurito)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.

# %%
