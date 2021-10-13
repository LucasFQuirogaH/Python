# %% [markdown]
# # Ok Andando!
# ## Retroceder nunca, rendirse jamas
# Los Imports
import pandas as pd
import os
import seaborn as sns
#--------------------------------------------------------------------
# Directorio Madre
DirectorioDeOrigen = "C:\Python/Unsam Python/Data"
#--------------------------------------------------------------------
# Nombres de los archivos
Archivo0 = "arbolado-en-espacios-verdes.csv"
Archivo1 = "arbolado-publico-lineal-2017-2018.csv"
#--------------------------------------------------------------------
#Direcciones exactas de los archivos
DireccionArchivo0 = os.path.join(DirectorioDeOrigen , Archivo0)
DireccionArchivo1 = os.path.join(DirectorioDeOrigen , Archivo1)
#--------------------------------------------------------------------
#Levanto los dataframe total por separados.
df_parques = pd.read_csv(DireccionArchivo0)
df_veredas = pd.read_csv(DireccionArchivo1)
#--------------------------------------------------------------------
# Eleccion de las columnas en cada archivo
col_parques = ["altura_tot" , "diametro"]
col_veredas = ["altura_arbol" , "diametro_altura_pecho"]
#--------------------------------------------------------------------
#Levanto los dataframe total por separados.
df_tipas_parques = df_parques[col_parques].copy()
df_tipas_veredas = df_veredas[col_veredas].copy()
#--------------------------------------------------------------------
# Cambio de nombre
df_tipas_parques = df_tipas_parques.rename({'altura_tot' : 'Altura' , 'diametro' : 'Diametro'} , axis = 1)
df_tipas_veredas = df_tipas_veredas.rename({'altura_arbol' : 'Altura' , 'diametro_altura_pecho' : 'Diametro'} , axis = 1)
#--------------------------------------------------------------------
# Agrego la columna Ambiente
df_tipas_parques = df_tipas_parques.assign(Ambiente = "Parque")
df_tipas_veredas = df_tipas_veredas.assign(Ambiente = "Vereda")
#--------------------------------------------------------------------
# Junto todo
df_tipas = pd.concat([df_tipas_veredas , df_tipas_parques])
#--------------------------------------------------------------------
# B O X P L O T para los diametros
df_tipas.boxplot('Diametro' , by = "Ambiente")
#--------------------------------------------------------------------
# Ahora las alturas
df_tipas.boxplot('Altura' , by = "Ambiente")
# %%
