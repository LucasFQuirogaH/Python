#--------------------------------------------------------------------
# %%
#
from sklearn.datasets import load_iris
iris_dataset = load_iris()
#--------------------------------------------------------------------
# %%
# Claves
print("Claves del diccionario iris_dataset:\n", iris_dataset.keys())
# %% Clasificacion
print("Target names:", iris_dataset['target_names'])

# %% Atributos
print("Feature names:\n", iris_dataset['feature_names'])
# %%
# Tipo de datos
print("Type of data:", type(iris_dataset['data']))
print("Shape of data:", iris_dataset['data'].shape)
# %%
print("First five rows of data:\n", iris_dataset['data'][:5])
# %%
#
print("Type of target:", type(iris_dataset['target']))
print("Shape of target:", iris_dataset['target'].shape)
print("Target:\n", iris_dataset['target'])
# %%
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
# Visualizacion
from sklearn.datasets import load_iris
iris_dataset = load_iris()
#--------------------------------------------------------------------
import pandas as pd
# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'] , columns = iris_dataset.feature_names)
# y hacemos una matriz de gráficos de dispersión, asignando colores según la especie
pd.plotting.scatter_matrix(iris_dataframe, c = iris_dataset['target'], figsize = (15, 15), marker = 'o', hist_kwds = {'bins': 20}, s = 40, alpha = 0.8)
# %%
iris_dataset['target']
# %%
