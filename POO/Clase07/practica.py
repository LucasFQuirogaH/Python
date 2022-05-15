# %%
import fileparse
import informe
import gzip
import pprint

# camion = fileparse.parse_csv('C:\Python/Unsam Python/Data/camion.csv', types=[str,int,float])
# with gzip.open('C:\Python/Unsam Python/Data/camion.csv.gz', 'rt') as file:
#     camion = fileparse.parse_csv(file, types=[str , int , float] , has_headers = True)
# pprint.pprint(camion)

# camion = fileparse.parse_csv('Data/camion.csv', types=[str,int,float])
# print(camion)

# with open ('C:\Python/Unsam Python/Data/camion.csv', "rt" , encoding = "utf8") as file:
#     camion = informe.leer_camion(file)
# print(camion)

with open('C:\Python/Unsam Python/Data/precios.csv', "rt", encoding = "utf8") as file:
    precios = informe.leer_precios(file)
pprint.pprint(precios)

precios = 15

# %%
assert True
# %%
assert False
# %%
def division(dividendo, divisor):
    '''Cálculo de la división
    Pre: Recibe dos números, divisor debe ser distinto de 0.
    Pos: Devuelve un número real, con el cociente de ambos.
    '''
    assert divisor != 0, 'El divisor no puede ser 0'
    return dividendo / divisor

# %%
print(division(5 , 0))
# %%
