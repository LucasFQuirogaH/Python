# Ejercicio 2: Agregar datos a una lista, simepre y cuando la lista sea menor a 120.
# Luego mostar la lista
# Usar while y for de ambas.

#Funciones-------------------------------------------------------------------------------------------------------------

def agrega() :
    ingresado = 0
    ingresado = int (input("Ingrese un nuevo dato: "))
    datos.append(ingresado)
    
def recorro (datos) :
    contador = 0
    for indice in datos :
        contador += 1
        print(f"Elemento {contador} : {indice}")



#Main------------------------------------------------------------------------------------------------------------------

datos =[1, 3]

# indicador = (len(datos))
# while (indicador < 12) :
#     agrega()
#     indicador += 1
# recorro(datos)

for indice in range(12 - len(datos)) :
    agrega()
recorro(datos)