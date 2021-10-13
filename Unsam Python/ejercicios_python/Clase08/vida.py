"""------------------------------------------------------------------------------------------------------------
Ejercicio 8.1: Segundos vividos
Escribí una función a la que le pasás tu fecha de nacimiento como cadena en formato 'dd/mm/AAAA'
(día, mes, año con 2, 2 y 4 dígitos, separados con barras normales) y te devuelve la cantidad de segundos
que viviste (asumiendo que naciste a las 00:00hs de tu fecha de nacimiento).
Guardá este código en el archivo vida.py.

Ing.Lucas F. Quiroga H. Fecha: 07/05/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%
from datetime import datetime


# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def SegundosVividos(fecha):
#Contrato: Se garantiza que entregando la fecha en el formato mencionado en la precondicion se devolvera un
# entero con la cantidad de segundos.
# Precondicion: Se ingresa una fecha en formato dd/mm/aaaa
# Poscondicion: Devuelve la cantidad de segundos vividos hasta el momento.
    from datetime import datetime
    fecha = "05/04/1982"
    fecha = fecha.split("/")
    dd = int(fecha[0])
    mm = int(fecha[1])
    aaaa = int(fecha[2])
    FechaFormato = datetime(aaaa , mm ,dd)
    return FechaFormato.timestamp()

## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    fecha = "05/04/1982"
    print("Hasta el momento llevas vivido: " , end = "" )
    print(SegundosVividos(fecha) , end = " ")
    print("segundos." , end = "")
    return None

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()
