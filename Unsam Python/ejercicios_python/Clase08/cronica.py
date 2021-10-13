"""------------------------------------------------------------------------------------------------------------
Ejercicio 8.2: Cuánto falta
Un conocido canal Argentino tiene por costumbre anunciar la cantidad de días que faltan para la próxima
primavera.
Escribí un programa que asista a los técnicos del canal indicándoles, al correr el programa el número que
deben poner en la placa.
Ing.Lucas F. Quiroga H. Fecha: 07/05/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%
from datetime import datetime, date

# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Placa -------------------------------------------------------------------------------------------
# %%
def placa():
#Contrato: La funcion devuelve la cantidad de dias que faltan para la llega de la primavera.
# Precondicion: Sin precondicion.
# Poscondicion: Devuelve un valor entero que representa los dias faltantes.-
    Hoy = date.today()
    FormatoHoy = date(year = Hoy.year, month = Hoy.month, day = Hoy.day)
    Primavera = date(year = Hoy.year, month = 9, day = 21)
    return ((Primavera - FormatoHoy).days)

## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    print("Faltan" , end = " ")
    print(placa() , end = " ")
    print("dias para la llegada de la primavera!!!!")
    return None

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()
