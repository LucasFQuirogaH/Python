# %%
# Import y levanto archivo
import pandas as pd
df = pd.read_csv('C:\Python/Unsam Python/Data/OBS_SHN_SF-BA.csv' , index_col=['Time'], parse_dates = True)
#--------------------------------------------------------------------
# %%
# 8.10 Tomo la porcion a ejecutar
dh = df['12-25-2014':].copy()
#--------------------------------------------------------------------
# %%
# Los deltas
delta_t = 0 # tiempo que tarda la marea entre ambos puertos
delta_h = 27 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
# %%
