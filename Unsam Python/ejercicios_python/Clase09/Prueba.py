#--------------------------------------------------------------------
# %%
#
import fileparse
import pprint
import lote
nom_archivo = "precios"
Nombre = 'C:\Python/Unsam Python/Data/' + nom_archivo + '.csv'
with open(Nombre , encoding = "utf8") as lines:
    precios = dict(fileparse.parse_csv(lines, types = [str,float], has_headers = False))
ListaDeFrutas = list(precios.keys())
ListaDePrecios = list(precios.values())
precios = [ lote.Lote(ListaDeFrutas[i] , 0 , ListaDePrecios[i]) for i in range(len(ListaDeFrutas))]
pprint.pprint (precios)
#--------------------------------------------------------------------
# %%
#
import fileparse
import pprint
import lote
nom_archivo = "camion"
Nombre = 'C:\Python/Unsam Python/Data/' + nom_archivo + '.csv'
with open(Nombre , encoding = "utf8") as lineas:
    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
camion = [ lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
pprint.pprint(camion)
# %%
