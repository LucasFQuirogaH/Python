"""------------------------------------------------------------------------------------------------------------
Costo Camion modificado para importar modulos.
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import ------------------------------------------------------------------------------------------------------
# %%
from django.http import HttpResponse


# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def saludo(request):
#Contrato:
# Precondicion:
# Poscondicion:
    return HttpResponse("Hola alumnos esta es nuestra primera vista")
