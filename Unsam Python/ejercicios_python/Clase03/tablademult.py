"""-----------------------------------------------------------------------------------------------------------------------
Ejercicio 3.17: Tablas de multiplicar
Escribí un programa tablamult.py que imprima de forma prolija las tablas de multiplicar del 1 al 9 usando f-strings.
Si podés, evitá usar la multiplicación, usando sólo sumas alcanza.
-----------------------------------------------------------------------------------------------------------------------"""
"""-----------------------------------------------------------------------------------------------------------------------
############################################ B U E N O  D A L E E ####################################################
-----------------------------------------------------------------------------------------------------------------------"""
Resultado = 0
tabla = []
Rayas = "--------------------------------------------------------"
print(f"{'':>5s} {0:>5d} {1:>5d} {3:>5d} {4:>5d} {5:>5d} {6:>5d} {7:>5d} {8:>5d} {9:>5d}")
print(f"{Rayas:>59s}")
for i in range (10):
    for j in range (9):
        tabla.append(Resultado)
        Resultado = Resultado + i
    tabla.append(Resultado)
    TablaDel = str(i) + ":"
    print(f"{TablaDel:>5s} {tabla[0]:>5d} {tabla[1]:>5d} {tabla[3]:>5d} {tabla[4]:>5d} {tabla[5]:>5d} {tabla[6]:>5d} {tabla[7]:>5d} {tabla[8]:>5d} {tabla[9]:>5d}")
    Resultado = 0
    tabla = []
    