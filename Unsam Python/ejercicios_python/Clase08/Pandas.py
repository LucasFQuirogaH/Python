"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R
------------------------------------------------------------------------------------------------------------"""
# %%
import pandas as pd
import os
import seaborn as sns

directorio = "C:\Python/Unsam Python/Data"
archivo = "arbolado-en-espacios-verdes.csv"
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)

# %%
# Perfecto visualizacion de los datos de los 5 primeros que es por defectos
df.head()

# %%
# Elige uno al azar
df.sample()

# Devuelve las columnas
df.columns

#Indice
df.index

# Describe para mostrar en detalle las columnas de interes
df[['altura_tot', 'diametro', 'inclinacio']].describe()

# Para ver solo una vez los nombres dentro de la columna que elijas
df['nombre_com'].unique()

# Cuantas se llaman ombu
df['nombre_com'] == 'Ombú'

# Se puede contar
(df['nombre_com'] == 'Ombú').sum()

# %%
# Cuenta la cantidad que hay
cant_ejemplares = df['nombre_com'].value_counts()
cant_ejemplares.head(10)

# %%
# Filtro Booleanos para generar vistas
df_jacarandas = df[df['nombre_com'] == 'Jacarandá']
df_jacarandas.head()

# Para seleccionar ciertas columns luego de haber elegido los jacarandas
cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]
df_jacarandas = df_jacarandas[[cols]] # Doble corchete se ve mejor
df_jacarandas.tail()

# %%
# Datos estadisticos de toda la tabla
df_jacarandas.describe()

# %%
# Para modificar es conveniente hacer una copia
df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()

# %%
# Para hacer graficos
df_jacarandas.plot.scatter(x = 'diametro', y = 'altura_tot')

# %%
# Para unos graficos mas lindos
sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')

# %%
# Especies como índice y sus respectivas cantidades como dato asociado.
cant_ejemplares = df['nombre_com'].value_counts()
cant_ejemplares.index

# %%
# Acceder a una fila a traves de la posicion o indice. Este es del total.
df.loc[165]

# %%
# Cantidad de ejemplares de eucalipto
cant_ejemplares.loc['Eucalipto']

# %%
# Para acceder por número de posición
df_jacarandas.iloc[0]

# %%
# Acceder a rebanadas (slices) usando iloc
cant_ejemplares.iloc[0:3]

# %%
# Podemos seleccionar tanto filas como columnas, si separamos con comas las respectivas selecciones
# Basicamente seleccionando una matriz cuadrada
df_jacarandas.iloc[-5:,2]

# %%
# Al tomar una sola columna obtenemos una serie en lugar de un DataFrame
df_jacarandas_diam = df_jacarandas['diametro']
type(df_jacarandas_diam)

type(df_jacarandas)

# %%
# A partir de una fecha creas 7 que son las consecutivas
pd.date_range('20200923', periods = 7)

# %%
# A partir de una fecha creas 7 que son las consecutivas pero con hora a las 14hs
pd.date_range('20200923 14:00', periods = 7)

# %%
# Ahora son 6 pero lo que cambia es la hora
pd.date_range('20200923 14:00', periods = 6, freq = 'H')

# %%
# Dataframe a partir de crear los indices y los periodos
pd.Series([1, 2, 3, 4, 5, 6], index = pd.date_range('20200923 14:00', periods = 6, freq = 'H'))

# %%
# Damos pasos cada un minuto generando la caminata
import numpy as np
idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()
s2.plot()

# %%
# Usando una media movil
w = 5 # ancho en minutos de la ventana
s3 = s2.rolling(w).mean()
s3.plot()

# %%
# Para ver 2 creas un dataframe
df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
df_series_23.plot()

# %%
# 12 personas caminando 8hs
horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']
df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()

w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas para los datos suavizados
df_walk_suav.plot()

# %%
# Para guardar es facil
df_walk_suav.to_csv('caminata_apostolica.csv')

# %%
# Cambiar nombres a las columnas
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
df = df.rename(columns={"A": "a", "B": "c"})
df.rename(columns={"A": "a", "B": "c"} , inplace=True)
df = df.rename({"A": "a", "B": "c"} , axis = 1)
df = df.rename({"A": "a", "B": "c"} , axis = "columns")
#--------------------------------------------------------------------
# %%
# Agregar una columna
df_tipas_parques = df_tipas_parques.assign(Ambiente = "Parque")

# %%
# Para juntar o concatenar
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])

#--------------------------------------------------------------------
# %%
# Con parse al final entiende la fecha aunque tenga otro formato
df = pd.read_csv('C:\Python/Unsam Python/Data/OBS_SHN_SF-BA.csv' , index_col=['Time'], parse_dates = True)



# %%
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R
------------------------------------------------------------------------------------------------------------"""

# %%
