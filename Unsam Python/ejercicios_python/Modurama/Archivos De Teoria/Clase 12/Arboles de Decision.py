"""------------------------------------------------------------------------------------------------------------
Aprendizaje basado en árboles de decisión utiliza un árbol de decisión como un modelo predictivo que mapea
observaciones sobre un artículo a conclusiones sobre el valor objetivo del artículo. Es uno de los enfoques
de modelado predictivo utilizadas en estadísticas, minería de datos y aprendizaje automático. Los modelos
de árbol, donde la variable de destino puede tomar un conjunto finito de valores se denominan árboles de
clasificación. En estas estructuras de árbol, las hojas representan etiquetas de clase y las ramas representan
las conjunciones de características que conducen a esas etiquetas de clase. Los árboles de decisión, donde la
variable de destino puede tomar valores continuos (por lo general números reales) se llaman árboles de regresión.
Los árboles de decisión se encuentran entre los algoritmos populares debido a su simplicidad.
En análisis de decisión, un árbol de decisión se puede utilizar para representar visualmente y de forma
explícita decisiones y toma de decisiones. En minería de datos, un árbol de decisión describe datos, pero
no las decisiones; más bien el árbol de clasificación resultante puede ser un usado como entrada para la
toma de decisiones. Esta página se ocupa de los árboles de decisión en la minería de datos.

Ing.Lucas F. Quiroga H. Fecha: 10/06/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
# Armas el arbol de decision
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()