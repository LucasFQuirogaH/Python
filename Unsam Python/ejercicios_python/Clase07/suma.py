"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%



# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def sumar_enteros(desde, hasta):
# Calcula la sumatoria de los números entre desde y hasta.
# Si hasta < desde, entonces devuelve cero.
# Pre: desde y hasta son números enteros
# Pos: Se devuelve el valor de sumar todos los números del intervalo
# [desde, hasta]. Si el intervalo es vacío se devuelve 0
    Suma = 0
    if desde >= hasta:
        return 0
    else:
        while (desde != hasta):
            Suma += desde
            desde +=1
        return Suma

## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def sumar_enteros_Gauss(desde, hasta):
# La gran Gauss
    if desde >= hasta:
        return 0
    else:
        return (int((hasta - 1) * hasta / 2))

## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    print(sumar_enteros_Gauss(1 , 100))

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()

