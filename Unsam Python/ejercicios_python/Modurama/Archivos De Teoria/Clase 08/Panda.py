#--------------------------------------------------------------------
# %%
#
import pandas as pd
#--------------------------------------------------------------------
df = pd.read_csv('C:\\Python/Unsam Python/Data/arbolado-en-espacios-verdes.csv')
# %%
df
# %%
df.head(0)

# %%
df.columns
# %%
df.index
# %%
df[['altura_tot', 'diametro', 'inclinacio']].describe()
# %%
df['nombre_com'].unique()
# %%
df['nombre_com']
# %%
df['nombre_com'] == 'Ombú'
# %%
(df['nombre_com'] == 'Ombú').sum()
# %%
df['nombre_com'].value_counts()
# %%
(df['nombre_com'].value_counts()).head(10)
# %%
df_jacarandas = df[df['nombre_com'] == 'Jacarandá']

# %%
df_jacarandas
# %%
jac = df_jacarandas[['altura_tot', 'diametro', 'inclinacio']]
#--------------------------------------------------------------------
jac
# %%
#
jac.tail([0:300])
#--------------------------------------------------------------------
# %%
#
jac.describe()

# %%
jac.plot.scatter(x = 'diametro' ,y = 'altura_tot')
# %%
import seaborn as sns
sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')
# %%
jac.iloc[45]
# %%
pd.date_range('20200923', periods = 7)
# %%
x = df['nombre_com'] == 'Jacarandá'

# %%
x.describe()
