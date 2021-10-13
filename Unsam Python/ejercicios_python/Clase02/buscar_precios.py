"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
########################################################################  Preliminares de la clase 02  #############################################################################
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

# creacion = open("Data/camion.csv" , "w")

# creacion.writelines(["Nombre",",","Cajones",",","Precio","\n"])
# creacion.writelines(["Lima",",","100",",","32.20","\n"])
# creacion.writelines(["Naranja",",","50",",","91.10","\n"])
# creacion.writelines(["Canqui",",","150",",","83.44","\n"])
# creacion.writelines(["Mandarina",",","200",",","51.23","\n"])
# creacion.writelines(["Durazno",",","95",",","40.37",",","\n"])
# creacion.writelines(["Mandarina",",","50",",","65.10","\n"])
# creacion.writelines(["Naranja",",","100",",","70.44","\n"])

# creacion.close()

# with open("C:\Python/Unsam Python/Data/camion.csv", "r") as creacion:
#     datosleidos = creacion.read()
# print(datosleidos)

# with open("Data/camion.csv", "r") as creacion:
#     datosleidos = creacion.read()
# print(datosleidos)

# with open("Data/camion.csv", "r") as creacion:
#     cabeceras = next(creacion)
#     print(cabeceras.split(","))
    # for line in creacion:
    #     print(line, end = "")
    
    
"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##################################################################################  Bueno Vamos  ####################################################################################
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 2.3: Precio de la naranja
El archivo Data/precios.csv contiene una serie de líneas con precios de venta de cajones en el mercado al que va el camión. El archivo se ve así:

"Lima",40.22
"Uva",24.85
"Ciruela",44.85
"Cereza",11.27
"Frutilla",53.72
...
Escribí un código que abra el archivo Data/precios.csv, busque el precio de la naranja y lo imprima en pantalla.

>>> f = open('../Data/precios.csv', 'rt')
...
>>> f.close()

El precio de la naranja es:  106.28
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""

# # Main----------------------------------------------------------
# EnLista =[]
# creacion = open("Data/precios.csv" , "r", encoding= "utf8")

# for line in creacion:
#     EnLista = line.split(",")
#     if "Naranja" in EnLista:
#         print(f"El precio de la Naranja es: {EnLista[1]}")
        
"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ejercicio 2.7: Buscar precios
A partir de lo que hiciste en el Ejercicio 2.3, escribí una función buscar_precio(fruta) que busque en archivo ../Data/precios.csv el precio de determinada fruta (o verdura) y lo
imprima en pantalla. Si la fruta no figura en el listado de precios, debe imprimir un mensaje que lo indique.

>>> buscar_precio('Frambuesa')
El precio de un cajón de Frambuesa es: 34.35
>>> buscar_precio('Kale')
Kale no figura en el listado de precios.
Guardá este código en un archivo buscar_precio.py para entregar al final de la clase.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Funciones ---------------------------------------------------------
def buscar_precio(fruta):
    EnLista = []
    bandera = False
    with open("Data/precios.csv", "r" , encoding="utf8") as creacion:
        for line in creacion:
            EnLista = line.split(",")
            if fruta in EnLista:
                print(f"Precio de {fruta} es: {EnLista[1]}")
                bandera = True
        if bandera is False:
            print("Lo siento, no disponemos de lo que busca")
    
# Main --------------------------------------------------------------
while (1):
    fruta = input ("Ingrese la fruta que necesita: ")
    buscar_precio(fruta)
    print("\n")
