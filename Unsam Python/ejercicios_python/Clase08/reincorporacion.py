"""------------------------------------------------------------------------------------------------------------
Ejercicio 8.3: Fecha de reincorporación
Si tenés una licencia por xaternidad que empieza el 26 de septiembre de 2020 y dura 200 días,
¿qué día te reincorporás al trabajo?
Ing.Lucas F. Quiroga H. Fecha: 07/05/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%
from datetime import datetime, date , timedelta


# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Reincorporacion ---------------------------------------------------------------------------------
# %%
def Reincorporacion():
#Contrato:La funcion devuelve un valor entero con la cantidad de dias que faltan desde la fecha 26/09/2020 para
# la reincorporacion por maternidad.
# Precondicion: Sin precondicion.
# Poscondicion: Fecha de la reincoporacion en formato timedelta.
    FormatoNacimiento = date(year = 2020, month = 9, day = 26)
    Reincorporacion = timedelta(days = 200)
    return ((FormatoNacimiento + Reincorporacion).strftime('%d/%m/%Y'))

## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    print("Fecha de reincorporacion: " , end = "")
    print(Reincorporacion())
    return None

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()
