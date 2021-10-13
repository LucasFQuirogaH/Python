"""-------------------------------------------------------------------------------------------------------------------------
Probamos en crear leer escribir los cvs
-------------------------------------------------------------------------------------------------------------------------"""
# Asi colocas para que funcione por consola
# Lista = open("C:\Python/Unsam Python/Data/Frutas.csv" , "w")

Lista = open("Data/Frutas.csv" , "w")

# Escribis las lineas

# Lista.writelines(["Fruta" , ";" , "Color" , ";" , "Cantidad" , "\n"])
# Lista.writelines(["Manzana" , ";" , "Roja" , ";" , "8" , "\n"])
# Lista.writelines(["Banana" , ";" , "Amarilla" , ";" , "16" , "\n"])
# Lista.writelines(["Naranja" , ";" , "Anaranjado" , ";" , "10" , "\n"])

# Lista.close()


# Lista = open("Data/Frutas.csv" , "r")

# datos = Lista.read() # Solo para leer
# print(datos)

# for i , line in enumerate(Lista):  # Esta enumera la fila y la presenta
#     print(i,line)

# for line in Lista:
#     # print(line)                      # 2 Maneras de mostrarlo
    
#     fila = line.split(",")
#     print(fila)
       
# import gzip
# with gzip.open('../Data/camion.csv.gz', 'rt') as f:

# Para saber en que directorio estoy
# import os
# print(os.getcwd())

# with open("Data/camion.csv", "r") as creacion: ## Otra manera de leer 
#     for line in creacion:
#         print(line, end = "")

# cabeceras = next(creacion) # Para serapar las cabeceras, con el for despues comienza en la linea siguiente
