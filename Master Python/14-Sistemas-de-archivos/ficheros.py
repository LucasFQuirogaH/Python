from io import open
import pathlib
import shutil
import os

"""---------------------------------------------------------------------------------------------------------------------
Abrir y/o crear un archivo
---------------------------------------------------------------------------------------------------------------------"""
#archivo = open ("14-Sistemas-de-archivos/fichero_texto.txt" , "a+")




#ruta = str(pathlib.Path().absolute()) + "/fichero_texo.txt" #Asi se muestra la ruta completa, consola de windows!
#ruta = open ("14-Sistemas-de-archivos/fichero_texo.txt")   #Asi se crea el archivo
#archivo = open (ruta , "a+")
# print(ruta)



"""---------------------------------------------------------------------------------------------------------------------
Escribir dentro de un archivo
---------------------------------------------------------------------------------------------------------------------"""

# #Escribir
# archivo.write("Hola como estas???")
# archivo.write("\nmi nombre es Lucas Quiroga")
# archivo.write("\nmuy contento de conocerte")

# #Cerrar
# archivo.close()

# #Leer
# archivo = open ("14-Sistemas-de-archivos/fichero_texto.txt" , "r")
# print (archivo.read())
# archivo.close()

#Leer por lienas y colocar en lista
#archivo = open ("14-Sistemas-de-archivos/fichero_texto.txt" ,  "r")
# print (archivo.readlines())
# lista = archivo.readlines()
# print(lista)
# print("\n")

# for frase in lista:
#     lista_de_frases = frase.split()
#     print(lista_de_frases)
    
#Copiar
# shutil.copyfile("14-Sistemas-de-archivos/fichero_texto.txt" , "11-Ejecicios2/ficheroCopiado.txt")

#Mover
# shutil.move("11-Ejecicios2/ficheroCopiado.txt" , "14-Sistemas-de-archivos/fichero_texto_Copiado.txt")

#eliminar
#os.remove("14-Sistemas-de-archivo/fichero_texto_copiado.txt")

#comprobar
if(os.path.isfile(os.path.abspath("./") + "/fichero_texto.txt")):
    print("El archivo esta")
else :
    print("El archivo no esta")
