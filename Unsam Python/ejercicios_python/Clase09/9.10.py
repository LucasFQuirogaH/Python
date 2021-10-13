#--------------------------------------------------------------------
# %%
#
# import lote
# c = lote.Lote('Peras', 100, 490.1)
# columnas = ['nombre', 'cajones']
# for colname in columnas:
#     print(colname, '=', getattr(c, colname))
# %%
import informe
from formato_tabla import crear_formateador, imprimir_tabla

camion = informe.leer_camion("camion")
formateador = crear_formateador('txt')

imprimir_tabla(camion, ['nombre','cajones'], formateador)
#--------------------------------------------------------------------
# %%
#