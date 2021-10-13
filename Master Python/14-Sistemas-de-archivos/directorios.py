from io import open
import pathlib
import shutil
import os
import os.path
# Crear una carpeta
# if not (os.path.isdir("./mi_carpeta")):


#Creas la carpeta
# os.mkdir("./mi_carpeta")

#Eliminar la carpeta
#os.rmdir("./mi_carpeta")

# open ("14-sistemas-de-archivos/mi_carpeta/Holamundo.txt" , "a+")
# open ("14-sistemas-de-archivos/mi_carpeta/archivo1.txt"  , "a+")
for fichero in (os.listdir("./mi_carpeta")) :
    print("fichero: " + fichero)
    

