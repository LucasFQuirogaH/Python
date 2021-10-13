aprobados = 0
desaprobados = 0

for indice in range(15):
    nota = int(input("Ingrese la nota del alumno: "))
    if nota >= 6:
        aprobados += 1
    else:
        desaprobados += 1

print(f"La cantidad de aprobados es de {aprobados} alumnos; mientras que los desaprobados asciende a {desaprobados}")
