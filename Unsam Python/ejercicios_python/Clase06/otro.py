# %%
import fileparse
import pprint

# %%
help(fileparse)

# %%
dir(fileparse)

# %%
camion = fileparse.parse_csv('C:\Python/Unsam Python/Data/camion.csv', select = ['nombre', 'cajones', 'precio'], types = [str, int, float] , has_headers = True)
pprint.pprint(camion)
# %%
