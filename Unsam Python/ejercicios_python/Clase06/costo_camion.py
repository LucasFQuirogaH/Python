"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import
# %%
from informe_funciones import leer_camion

# Funciones ---------------------------------------------------------------------------------------------------
## Funcion: Costo camion. -------------------------------------------------------------------------------------
# %%
def costo_camion(archivo):
    import csv
    CamionLeido = leer_camion(archivo)
# Main  --------------------------------------------------------------------------------------------------------
# %%

costo_camion("camion")
