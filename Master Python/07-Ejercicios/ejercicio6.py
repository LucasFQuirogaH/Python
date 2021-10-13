indice = 0
index = 0
for indice in range (9) :
    print(f"La tabla del {indice + 1} se compone de: ")
    print("\n")
    for index in range (9):
        print(f"{indice + 1} x {index + 1} = {(indice + 1) * (index + 1)}")
    print("\n")
    print(f"Fin de la tabla del {indice + 1}")
    print("\n")
print("\n")
print("Fin total")
