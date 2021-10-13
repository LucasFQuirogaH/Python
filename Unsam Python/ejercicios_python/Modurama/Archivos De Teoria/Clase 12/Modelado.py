"""------------------------------------------------------------------------------------------------------------
Ahora vamos a construir nuestro primer modelo. Usaremos un algoritmo sencillo que se llama de "vecinos más
cercanos" (K-nearest neighbors_ en inglés, ver wikipedia). Lo entrenaremos con los datos de entrenamiento y al
consultarle por un nuevo dato (de los de testing) lo que hará el algoritmo es buscar al dato de entrenamiento
más cercano en el espacio de atributos y asignarle al nuevo dato la especie de esa flor. En otras palabras:
cuando le preguntemos por la especie de una flor nueva va a contestarnos con la especie de la flor "más
cercana" en el espacio de atributos (ancho y largo del pétalo y el sépalo).
Ing.Lucas F. Quiroga H. Fecha: 17/04/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
# Importas para poder
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
iris_dataset = load_iris()
#--------------------------------------------------------------------
# Separas datos en 75 para aprender y 25 para probar
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state = 0)
#--------------------------------------------------------------------
# Creo una clase KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)
#--------------------------------------------------------------------
# Lo pones a entrenar
knn.fit(X_train, y_train)
#--------------------------------------------------------------------
# Ahora podemos predecir,por ejemplo la flor que podria ser a partir
# de sus medidas. Creas un X nuevo.
import numpy as np
X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new.shape:", X_new.shape)
#--------------------------------------------------------------------
# Graficamos con punto rojo para ver como se ubica. C en la primera
# linea implica que segun el y colocara el color. Abajo como es uno
# le pones un color cualquiera.
import matplotlib.pyplot as plt
plt.scatter(X_train[:, 1], X_train[:, 3], c = y_train)
plt.scatter(X_new[:, 1], X_new[:, 3], c = 'red')
#--------------------------------------------------------------------
# Prediccion del modelo entrenado
prediction = knn.predict(X_new)
print("Predicción:", prediction)
print("Nombre de la Especie Predicha:", iris_dataset['target_names'][prediction])
#--------------------------------------------------------------------
# Usamos el 25% de los datos etiquetados que guardamos para evaluar
# que tan bien funciona nuestro clasificador.
y_pred = knn.predict(X_test)
print("Predicciones para el conjunto de Test:\n", y_pred)
print("Etiquetas originales de este conjunto:\n", y_test)
#--------------------------------------------------------------------
# Medimos el éxito calculando la fracción de clasificaciones bien
# hechas (calculamos el promedio de "1 si está bien, 0 si está mal
print(y_pred == y_test)
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))
#--------------------------------------------------------------------
# Usando comando score
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))
"""------------------------------------------------------------------------------------------------------------
Lo que hicimos hasta ahora fue:

1) Separar los datos en dos conjuntos: train y test.
2) Sefinir un clasificador knn y entrenarlo con los datos de training.
3) Evaluar el clasificador con los datos de testing.
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'])

knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train, y_train)
print("Test set score: {:.2f}".format(knn.score(X_test, y_test)))
------------------------------------------------------------------------------------------------------------"""