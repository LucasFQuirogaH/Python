"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import ------------------------------------------------------------------------------------------------------
import csv
# %%
# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def costo_camion(nombre):
#Contrato:
# Precondicion:
# Poscondicion:
    direccion = "C:\\Users\\inglu\\Documents\\Cursos\\Python\\Unsam Python Dupli\\Data\\" + str(nombre) + ".csv"
    suma = 0
    with open(direccion , 'rt' , encoding="utf8") as f:
        Lectura = csv.reader(f) #Lee en formato arreglo para trabajar con partes
        next(Lectura) #Se queda con las cabeceras
        for line in Lectura:
            suma = suma + float(line[1]) * float(line[2])
    return suma
## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    presenta = costo_camion('camion')
    print(presenta)
    return None
    
# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()