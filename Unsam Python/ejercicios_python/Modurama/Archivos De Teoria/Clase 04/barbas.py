#--------------------------------------------------------------------
# %%
#
import csv
f = open('C:\\Python/Unsam Python/Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)
#--------------------------------------------------------------------
# %%
#
headers
# %%
select = ['nombre', 'cajones', 'precio']
# %%
select
#--------------------------------------------------------------------
# %%
#
indices = [headers.index(ncolumna) for ncolumna in select]
#--------------------------------------------------------------------
# %%
#
indices
# %%
row = next(rows)
record = {ncolumna: row[index] for ncolumna, index in zip(select, indices)}
#--------------------------------------------------------------------
# %%
#
record
# %%
camion = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]
# %%
camion
# %%]
