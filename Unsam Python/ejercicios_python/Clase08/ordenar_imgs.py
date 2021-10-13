"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
import os
# %%

# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def ManipulaStrings(DirectorioActual , nombre):
#Contrato: Toma el nombre de un archivo y devuelve la fecha y el nombre corregido.
# Precondicion:
# Poscondicion:

    """------------------------------------------------------------------------------------------------------------
    S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R
    ------------------------------------------------------------------------------------------------------------"""
    # %%
    import os
    name = "Juanito_20210823.png"
    DirectorioActual = "C:\Python/Unsam Python/Data/original/original"
    DireccionExacta = DirectorioActual + "/" + name

    Fecha = []
    NombreModificado = []
    for c in name:
        if c in "0123456789":
            Fecha.append(c)
        elif c == "_":
            pass
        else:
            NombreModificado.append(c)

    Fecha = str("".join(Fecha))
    NombreModificado = str("".join(NombreModificado))

    # print(DireccionExacta)
    print(Fecha)
    print(NombreModificado)
    # os.chdir(DirectorioActual)
    # os.rename(name , )

    # %%
    """------------------------------------------------------------------------------------------------------------
    S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R
    ------------------------------------------------------------------------------------------------------------"""

    return Fecha , NombreModificado


## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def YaVemos(DirectorioOriginal , DirectorioDestino):
#Contrato: Toma el nombre de un archivo y devuelve la fecha y el nombre corregido.
# Precondicion:
# Poscondicion:

    """------------------------------------------------------------------------------------------------------------
    S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R
    ------------------------------------------------------------------------------------------------------------"""
    # %%
    import os
    DirectorioOriginal = os.path.join("c:\\" , "Python" , "Unsam Python" , "Data" , "ordenar")
    DirectorioDestino = os.path.join("c:\\" , "Python" , "Unsam Python" , "Data" , "ordenados")
    for root, dirs, files in os.walk(DirectorioOriginal):
        for name in files:
            if ".png" in name:
                DirectorioDelName = os.getcwd()
                Fecha , NombreModificado = ManipulaStrings(DirectorioActual , name)
                #Funcion2
        for name in dirs:
            if ".png" in name:
                DirectorioDelName = os.getcwd()
                ManipulaStrings(DirectorioActual , name)
                #Funcion2

    # %%
    """------------------------------------------------------------------------------------------------------------
    S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R
    ------------------------------------------------------------------------------------------------------------"""
    return None


## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main(Parametros):
# El main como programa principal
# El main como programa principal
# DirectorioOriginal = ""
# DirectorioDestino = ""
# if len(sys.argv) != 3:
# # Distinto de 3 porque en este ejemplo esta el .py y 2 argumentos
#     raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
# #sys.argv[0] es el .py que se esta ejecutando, sys.argv[1 el primer argumento despues de llamar al .py]
# archivo1 = sys.argv[1]
# archivo2 = sys.argv[2]

    DirectorioOriginal = "C:\Python/Unsam Python/Data/original"
    #Crear el directorio ordenados
    YaVemos(DirectorioOriginal , DirectorioDestino)

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    # main(sys.argv)
    main()

"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R
------------------------------------------------------------------------------------------------------------"""

"""
import os
os.system("cls")
os.getcwd() # Para saber donde estas parado
os.chdir("C:\Python/Unsam Python/ejercicios_python")
#Para escribir una sola vez el directorio
Directorio = os.path.join("c:\" , "Python" , "Unsam Python" , "ejercicios_python")
os.listdir(directorio)
#Crear un directorio
os.mkdir("Directorio") # Tenes que estar parado en el directorio
# Para renombrar
os.rename("Carpeta" , "nuevo nombre")
# Para borrar un directorio vacio
os.rmdir("Carpeta")
# Para borrar un directorio con datos
import shutil
shutil.rmtree('carpeta')
os.listdir()
# Para borrar un archivo
os.remove("archivo.txt")

# Lista todos los directorios y archivos en todas las carpetas de la raiz donde estas parado
import os
Directorio = os.path.join("c:\" , "Python" , "Unsam Python" , "Data" , "ordenar")
for root, dirs, files in os.walk(Directorio):
    for name in files:
        if ".png" in name:
            print(os.path.join(root, name))
    for name in dirs:
        if ".png" in name:
            print(os.path.join(root, name))

#Cambiar atributos a un archivo
import os
import datetime
import time
camino = './rebotes.py'
stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))
fecha_acceso = datetime.datetime(year = 2017, month = 9, day = 21, hour = 19, minute =51, second = 0)
fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute =9, second = 24)
ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()
os.utime(camino, (ts_acceso, ts_modifi))
stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))
"""
