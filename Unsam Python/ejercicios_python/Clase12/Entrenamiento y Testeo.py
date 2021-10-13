"""------------------------------------------------------------------------------------------------------------
Entrenamiento y testo
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
#
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris_dataset = load_iris()
#--------------------------------------------------------------------
# %%
# Separas datos en 75 para aprender y 25 para probar
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 0)
#--------------------------------------------------------------------
# %%
#
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
# %%
