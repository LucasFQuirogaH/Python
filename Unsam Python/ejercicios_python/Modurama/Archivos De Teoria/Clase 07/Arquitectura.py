"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import ------------------------------------------------------------------------------------------------------
# %%



# Funciones ---------------------------------------------------------------------------------------------------






## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    return None

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()

"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%



# Funciones ---------------------------------------------------------------------------------------------------






## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main(Parametros):
# El main como programa principal
# El main como programa principal
archivo1 = ""
archivo2 = ""
if len(sys.argv) != 3:
# Distinto de 3 porque en este ejemplo esta el .py y 2 argumentos
    raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
#sys.argv[0] es el .py que se esta ejecutando, sys.argv[1 el primer argumento despues de llamar al .py]
archivo1 = sys.argv[1]
archivo2 = sys.argv[2]

informe_camion(archivo1 , archivo2)
# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main(sys.argv)

