"""------------------------------------------------------------------------------------------------------------
Ejercicio 8.5: Recorrer el árbol de archivos
Escribí un programa que dado un directorio, imprima en pantalla los nombres de todos los archivos .png que se
encuentren en algún subdirectorio del él.
Observación: Al final, tu script debería poder ejecutarse desde la línea de comandos recibiendo como parámetro
el directorio a leer original. En la Sección 7.3 dimos un modelo de script que te puede servir.
Guardá el script resultante en un archivo listar_imgs.py.

Ing.Lucas F. Quiroga H. Fecha: 11/05/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
import os
import sys
# %%

# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Impresion ---------------------------------------------------------------------------------------
# %%
def Impresion(Directorio):
# Contrato: La presente funcion imprime por pantalla las rutas de los archivos .png dentro de la carpeta
# ordenar, ubicada dentro del direcorio Data.
# Precondicion: Se suministra solo el nombre de al carpeta a analizar, por consola y seguida del nombre
# de este archivo en ejecucion.
# Poscondicion: Sin devolucion. Solo imprime por pantalla rutas de archivos especificados en el codigo.
    for root, dirs, files in os.walk(Directorio):
        for name in files:
            if ".png" in name:
                print(os.path.join(root, name))
        for name in dirs:
            if ".png" in name:
                print(os.path.join(root, name))
        return None

## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main(Parametros):
# El main como programa principal
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'Por ejemplo \"ordenar\" que debe estar en la carpeta Data')
    Directorio = os.path.join("c:\\" , "Python" , "Unsam Python" , "Data" , sys.argv[1])
    Impresion(Directorio)
# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main(sys.argv)