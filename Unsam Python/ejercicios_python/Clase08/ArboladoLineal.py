# %%
# Los imports
import pandas as pd
import os
import seaborn as sns

# %%
# Levantando el archivo
DirectorioDeOrigen = "C:\Python/Unsam Python/Data"
Archivo = "arbolado-publico-lineal-2017-2018.csv"
DireccionExacta = os.path.join(DirectorioDeOrigen , Archivo)
df_lineal = pd.read_csv(DireccionExacta)
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']

# %%
# Las diez especies más frecuentes
# Solo la columna de los nombres cientificos, osea los nombres
dfConNombres = df_lineal[["nombre_cientifico"]]
# Cuenta la cantidad.
dfContados = dfConNombres.value_counts()
# Solo le pedis los primeros 10
dfContados.iloc[0:10]

# %%
# Trabajaremos con las siguientes especies seleccionadas
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

#Las seleccionamos asi:
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

# %%
# B O X P L O T (Diagrama de Caja y Bigote)
df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
# %%
# B O X P L O T Ahora con altos
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')

# %%
sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
# %%
