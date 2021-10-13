"""------------------------------------------------------------------------------------------------------------
El ultimo!! 12.12
Ing.Lucas F. Quiroga H. Fecha: 11/06/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------------------------------------------------
# %%
# Importas para poder
from joblib.logger import PrintTime
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris_dataset = load_iris()
#--------------------------------------------------------------------------------------------------------------
# Separas datos en 75 para aprender y 25 para probar
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'])

#--------------------------------------------------------------------------------------------------------------
# Creo las clases
#--------------------------------------------------------------------------------------------------------------
# Creo una clase KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)
#--------------------------------------------------------------------
# Creo una clase KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()

#--------------------------------------------------------------------------------------------------------------
# Ponemos a entrenar
#--------------------------------------------------------------------------------------------------------------
# Pones a entrenar a vecinos cercanos
knn.fit(X_train, y_train)
#--------------------------------------------------------------------
# Pones a entrenar a arboles
clf.fit(X_train, y_train)

#--------------------------------------------------------------------------------------------------------------
# Creo un x de prueba
#--------------------------------------------------------------------------------------------------------------
import numpy as np
X_new = np.array([[5, 2.9, 1, 0.2]])

#--------------------------------------------------------------------------------------------------------------
# Graficas el punto rojo.
#--------------------------------------------------------------------------------------------------------------
# import matplotlib.pyplot as plt
# plt.scatter(X_train[:, 1], X_train[:, 3], c = y_train)
# plt.scatter(X_new[:, 1], X_new[:, 3], c = 'red')

#--------------------------------------------------------------------------------------------------------------
# Prediccion del modelo entrenado y print en pantalla
#--------------------------------------------------------------------------------------------------------------
# Prediccion de Knn
prediction = knn.predict(X_new)
print("Prediccion del modelo Knn ----------------")
print("Predicción:", prediction)
print("Nombre de la Especie Predicha:", iris_dataset['target_names'][prediction])
#--------------------------------------------------------------------
# Prediccion de Knn
print("#-----------------------------------------")
prediction = clf.predict(X_new)
print("Prediccion del modelo Clf ----------------")
print("Predicción:", prediction)
print("Nombre de la Especie Predicha:", iris_dataset['target_names'][prediction])

#--------------------------------------------------------------------------------------------------------------
# Probamosque tan bien funciona nuestro predictor
#--------------------------------------------------------------------------------------------------------------
# Que tan bien funciona nuestro clasificador. Knn.-
y_pred = knn.predict(X_test)
print("#--------------------------------------------------------------------")
print("Predicciones con Knn -----------------------------")
print("Predicciones para el conjunto de Test:\n", y_pred)
print("Etiquetas originales de este conjunto:\n", y_test)
#--------------------------------------------------------------------
# Que tan bien funciona nuestro clasificador. Clf.-
y_pred2 = clf.predict(X_test)
print("#--------------------------------------------------------------------")
print("Predicciones con Clf -----------------------------")
print("Predicciones para el conjunto de Test:\n", y_pred2)
print("Etiquetas originales de este conjunto:\n", y_test)
#--------------------------------------------------------------------------------------------------------------
# Usando comando score
print("Predicciones con Knn -----------------------------")
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))
#--------------------------------------------------------------------
print("#--------------------------------------------------------------------")
print("Predicciones con Clf -----------------------------")
print("Test set score: {:.2f}".format(clf.score(X_test, y_test)))
# %%
