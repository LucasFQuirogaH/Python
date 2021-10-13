"""---------------------------------------------------------------------------------------------------------------------
Activamos la clase!!!!!
---------------------------------------------------------------------------------------------------------------------"""
from coche import coche

# fitito = coche("azul" , "Fiat 600" , 90)
# print(fitito.getTotal())

Gol = coche("Blanco" , "Gold Trend 1.6" , 165)
print(Gol.getTotal())

#Tipado
if type(Gol) == coche :
    print("La clase es de tipo coche")
    
