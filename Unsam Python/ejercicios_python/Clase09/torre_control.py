#--------------------------------------------------------------------
# %%
# Clase Padre
class Cola:
    def __init__(self):
        self.items = []
    def encolar(self, x):
        self.items.append(x)
    def desencolar(self):
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)
    def esta_vacia(self):
        return len(self.items) == 0
    def __str__(self):
        String = ["Hay esperando: "]
        for item in self.items:
            MasString = '     ' + object.__str__(item)
            String.append(MasString)
        return str(",".join(String))

#--------------------------------------------------------------------
# %%
# Clase Arribos
class Arribos(Cola):
    def nuevo_arribo(self , avion):
        Arribos().encolar(avion)
    def __str__(self):
        # String = ["Hay esperando: "]
        # for item in self.items:
        #     MasString = '     ' + object.__str__(item)
        #     String.append(MasString)
        # return str(",".join(String))
        return f'{self.items}'

#--------------------------------------------------------------------
# %%
# Clase partidas
class Partidas(Cola):
    def nueva_partida(self , avion):
        Partidas().encolar(avion)
    def __str__(self):
        String = ["Hay esperando: "]
        for item in self.items:
            MasString = '     ' + object.__str__(item)
            String.append(MasString)
        return str(",".join(String))

#--------------------------------------------------------------------
# %%
# Funciones a parte
def ver_estado():
    print(Arribos)
    print(Partidas)

#--------------------------------------------------------------------
# %%
# Main de Prueba
ver_estado()

# %%
Arribos().nuevo_arribo("AR2804")

# %%
Partidas().nueva_partida("AR9100")