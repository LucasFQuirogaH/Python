"""--------------------------------------------------------------------------------------------------------------------------
Vamos a jugar al truco!!
--------------------------------------------------------------------------------------------------------------------------"""


"""-------------------------------------------------------------------------------------------------------------------------
Para el calculo de 31 de mano:
1-) Tener el 7 y el 4, pero no el 6 ni el 5. Por lo tanto de 38C1 manos donde hay 2 cartas especificas quito 2 manos.
2-) Tener el 6 y el 5, pero no tener el 7 del mismo palo. Para 38C1 manos donde hay 2 cartas especidicas quito una mano.
-------------------------------------------------------------------------------------------------------------------------"""

# import random
# import copy
# Valores = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 10 , 11 , 12]
# Palos = ["Oro" , "Copa" , "Espada" , "Basto"]
# Naipes = [(Valor , Palo) for Valor in Valores for Palo in Palos]

# P31 = 4 * (36 + 37) / 9880
# print(f"El calculo de 31 en una mano de truco es: {round(P31 , 5)}")
# print ("Pero para estimar, juguemos...")
# Contador31 = 0
# Cuatro = -1
# Cinco = -1
# Seis = -1
# Siete = -1
# PaloCuatro = ""
# PaloCinco = ""
# PaloSeis = ""
# PaloSiete = ""
# N = 10000
# for i in range(N):
#     Mazo = copy.deepcopy(Naipes)
#     random.shuffle(Mazo)
#     Mano = [Mazo.pop() , Mazo.pop() , Mazo.pop()]
#     # Mano = [(4 , "Oro") , (7 , "Oro") , (5 , "Oro")]
#     for Carta in Mano:
#         if Carta[0] == 4:
#             Bandera = 1
#             Cuatro = 1
#             PaloCuatro = Carta[1]
#         elif Carta[0] == 5:
#             Bandera = True
#             Cinco = 1
#             PaloCinco = Carta[1]
#         elif Carta[0] == 6:
#             Bandera = True
#             Seis = 1
#             PaloSeis = Carta [1]
#         elif Carta[0] == 7:
#             Bandera = True
#             Siete = 1
#             PaloSiete = Carta[1]

#     if (Cuatro == 1) and (Siete == 1) and (PaloCuatro == PaloSiete):
#         if Seis == -1 and Cinco == -1:
#             Contador31 += 1
#         elif Seis == 1 and (PaloSeis != PaloCuatro):
#             Contador31 += 1
#         elif Cinco == 1 and PaloCinco != PaloCuatro:
#             Contador31 += 1
            
#     if (Cinco == 1) and (Seis == 1) and (PaloCinco == PaloSeis):
#         if Siete == -1:
#             Contador31 += 1
#         elif Siete == 1 and (PaloCinco != PaloSiete):
#             Contador31 += 1

#     if Bandera:
#         Cuatro = -1
#         Cinco = -1
#         Seis = -1
#         Siete = -1
#         PaloCuatro = ""
#         PaloCinco = ""
#         PaloSeis = ""
#         PaloSiete = ""
# print()
# print(Contador31)
# print()
# print(f"Se jugo {N} veces obteniendo una probabilidad de {Contador31/N}")



"""-------------------------------------------------------------------------------------------------------------------------
Para el calculo de 32 de mano:
1-) Tener el 7 y el 5, y que no te toque el 6 del mismo palo.
-------------------------------------------------------------------------------------------------------------------------"""
# import random
# import copy
# Valores = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 10 , 11 , 12]
# Palos = ["Oro" , "Copa" , "Espada" , "Basto"]
# Naipes = [(Valor , Palo) for Valor in Valores for Palo in Palos]

# P32 = 4 * 37 / 9880
# print(f"El calculo de 32 en una mano de truco es: {round(P32 , 5)}")
# print ("Pero para estimar, juguemos...")
# Contador32 = 0
# Cinco = -1
# Seis = -1
# Siete = -1
# PaloCinco = ""
# PaloSeis = ""
# PaloSiete = ""
# Bandera = False
# N = 100000
# for i in range(N):
#     Mazo = copy.deepcopy(Naipes)
#     random.shuffle(Mazo)
#     Mano = [Mazo.pop() , Mazo.pop() , Mazo.pop()]
#     # Mano = [(4 , "Oro") , (7 , "Oro") , (5 , "Oro")]
#     for Carta in Mano:
#         if Carta[0] == 5:
#             Bandera = True
#             Cinco = 1
#             PaloCinco = Carta[1]
#         elif Carta[0] == 7:
#             Bandera = True
#             Siete = 1
#             PaloSiete = Carta[1]
#     if (Cinco == 1) and (Siete == 1) and (PaloCinco == PaloSiete):
#         if Seis == -1:
#             Contador32 += 1
#         elif Seis == 1 and (PaloSeis != PaloCinco):
#             Contador32 += 1
#     if Bandera:
#         Cinco = -1
#         Seis = -1
#         Siete = -1
#         PaloCinco = ""
#         PaloSiete = ""
# print()
# print(Contador32)
# print()
# print(f"Se jugo {N} veces obteniendo una probabilidad de {Contador32/N}")

"""-------------------------------------------------------------------------------------------------------------------------
Para el calculo de 33 de mano:
1-) Tener el 7 y el 6.
-------------------------------------------------------------------------------------------------------------------------"""
import random
import copy
Valores = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 10 , 11 , 12]
Palos = ["Oro" , "Copa" , "Espada" , "Basto"]
Naipes = [(Valor , Palo) for Valor in Valores for Palo in Palos]

P33 = 4 * 38 / 9880
print(f"El calculo de 33 en una mano de truco es: {round(P33 , 5)}")
print ("Pero para estimar, juguemos...")
Contador33 = 0
Seis = -1
Siete = -1
PaloSeis = ""
PaloSiete = ""
Bandera = False
N = 100000
for i in range(N):
    Mazo = copy.deepcopy(Naipes)
    random.shuffle(Mazo)
    Mano = [Mazo.pop() , Mazo.pop() , Mazo.pop()]
    # Mano = [(4 , "Oro") , (7 , "Oro") , (5 , "Oro")]
    for Carta in Mano:
        if Carta[0] == 6:
            Bandera = True
            Seis = 1
            PaloSeis = Carta[1]
        elif Carta[0] == 7:
            Bandera = True
            Siete = 1
            PaloSiete = Carta[1]
    if (Seis == 1) and (Siete == 1) and (PaloSeis == PaloSiete):
            Contador33 += 1
    if Bandera:
        Seis = -1
        Siete = -1
        PaloSeis = ""
        PaloSiete = ""
print()
print(Contador33)
print()
print(f"Se jugo {N} veces obteniendo una probabilidad de {Contador33/N}")