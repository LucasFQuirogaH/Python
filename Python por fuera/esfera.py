"""------------------------------------------------------------------------------------------------------------
Creando de vuelta la esfera
Ing.Lucas F. Quiroga H. Fecha: 15/11/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import ------------------------------------------------------------------------------------------------------
# %%
from math import pi

# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Muestra el resultado ----------------------------------------------------------------------------
# %%
def ShowResults(Volume):
#Contrato:
# Precondicion:
# Poscondicion:
    print(f"El resultado del calculo del volumen es: {Volume}")
    return None
## Funciones: Calculador de volumen ---------------------------------------------------------------------------
def VolumeCalculate(radio):
#Contrato:
# Precondicion:
# Poscondicion:
    Volume = (4/3) * pi * (radio ** 3)
    ShowResults(Volume)
    return None

## Funciones: Pedido de radio ---------------------------------------------------------------------------------
# %%
def GetRadio():
#Contrato:
# Precondicion:
# Poscondicion:
    radio = float(input("Ingrese en radio para calcular el volumen de la esfera: "))
    VolumeCalculate(radio)
    return None

## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    GetRadio()
    return None
    
# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()