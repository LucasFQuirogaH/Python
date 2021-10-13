#--------------------------------------------------------------------
# %%
#
#--------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#--------------------------------------------------------------------
x = np.array([55.0, 38, 68, 70, 53, 46, 11, 16, 20, 4])
y = np.array([153.0, 98, 214, 220, 167, 145, 41, 63, 65, 25])
plt.scatter(x = x, y = y)
plt.title('scatterplot de los datos')
plt.show()
#--------------------------------------------------------------------------------------------------------------
# %%
#--------------------------------------------------------------------------------------------------------------
# C A L C U L O   D E L   P R O M E D I O   D E   E R R O R E S   C U A D R A T I C O S   P O R   N U M P Y
error= (1/n) * np.sum(np.square(predictions - labels))
#--------------------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------------
# %%
#--------------------------------------------------------------------------------------------------------------
# C A L C U L O   D E L   P R O M E D I O   D E   E R R O R E S   C U A D R A T I C O S  P O R   S K L E A R N
#--------------------------------------------------------------------------------------------------------------
from sklearn.metrics import mean_squared_error
mean_squared_error(predictions - labels)
#--------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------
# C A L C U L O   N A T I V O   D E L   P R O M E D I O   D E   E R R O R E S   C U A D R A T I C O S
#--------------------------------------------------------------------------------------------------------------
errores = y - (x*a + b)
print("ECM", (errores**2).mean())
#--------------------------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------------------------
# %%
#--------------------------------------------------------------------------------------------------------------
# C A L C U L O   D E L   C O E F I C I E N T E S    P O R    F O R M U L A    N A T I V A
#--------------------------------------------------------------------------------------------------------------
def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b
#--------------------------------------------------------------------------------------------------------------




# E J E R C I C I O   C O M P L E T O  ------------------------------
# %%
#
import matplotlib.pyplot as plt
import numpy as np
#--------------------------------------------------------------------
def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b
#--------------------------------------------------------------------
N = 50
minx = 0
maxx = 500
x = np.random.uniform(minx, maxx, N)
r = np.random.normal(0, 25, N) # residuos simulados con distribucion gausseana
y = 1.3*x + r
#--------------------------------------------------------------------
# Calculo de los coeficientes y ploteo
a, b = ajuste_lineal_simple(x, y)
grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
grilla_y = grilla_x*a + b
plt.scatter(x = x, y = y)
plt.title('y ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
#--------------------------------------------------------------------
# Calculo de errores y printeo
errores = y - (x*a + b)
print("ECM", (errores**2).mean())
#--------------------------------------------------------------------
# %%


"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
xc = x**2
ap, bp = ajuste_lineal_simple(xc, y)
grilla_y_p = (grilla_x**2)*ap + bp
plt.scatter(x,y)
plt.plot(grilla_x, grilla_y, c = 'green')
plt.plot(grilla_x, grilla_y_p, c = 'red')
plt.title('ajuste lineal con x^2')
plt.show()


#--------------------------------------------------------------------------------------------------------------
# Ejercicio cuadratico
np.random.seed(3141) # semilla para fijar la aleatoriedad
N=50
indep_vars = np.random.uniform(size = N, low = 0, high = 10)
r = np.random.normal(size = N, loc = 0.0, scale = 8.0) # residuos
dep_vars = 2 + 3*indep_vars + 2*indep_vars**2 + r # relación cuadrática
#--------------------------------------------------------------------


"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R   A H O R A   C O N   S K L E A R N
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
#
import numpy as np
import pandas as pd
from sklearn import linear_model
#--------------------------------------------------------------------
x = np.array([55.0, 38, 68, 70, 53, 46, 11, 16, 20, 4]) # mismos datos x, y
y = np.array([153.0, 98, 214, 220, 167, 145, 41, 63, 65, 25])
datosxy = pd.DataFrame({'superficie' : x , 'Precio' : y}) # paso los datos a un dataframe
#--------------------------------------------------------------------
#--------------------------------------------------------------------
# %%
#
datosxy
#--------------------------------------------------------------------
# %%
ajus = linear_model.LinearRegression() # llamo al modelo de regresión lineal
ajus.fit(datosxy[['x']], datosxy['y']) # ajusto el modelo
#--------------------------------------------------------------------
grilla_x = np.linspace(start = 0, stop = 70, num = 1000)
grilla_y = ajus.predict(grilla_x.reshape(-1,1))
#--------------------------------------------------------------------
datosxy.plot.scatter('x','y')
plt.title('ajuste lineal usando sklearn')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.show()

"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R
------------------------------------------------------------------------------------------------------------"""
# %%
help(pd.DataFrame)

# %%
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R  -  S E P A R A D O R
------------------------------------------------------------------------------------------------------------"""


"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
#
import numpy as np
from sklearn import linear_model
import pandas as pd
#--------------------------------------------------------------------
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
antigüedad = [50.0, 5.0, 25.0, 70.0]
#--------------------------------------------------------------------
data_deptos = pd.DataFrame({'alquiler': alquiler, 'superficie': superficie, 'antigüedad': antigüedad})
#--------------------------------------------------------------------
X = pd.concat([data_deptos.superficie,data_deptos.antigüedad], axis = 1)
#--------------------------------------------------------------------
ajuste_deptos = linear_model.LinearRegression()
ajuste_deptos.fit(X,data_deptos.alquiler)
#--------------------------------------------------------------------
errores = data_deptos.alquiler - (ajuste_deptos.predict(X))
print(errores)
print("ECM:", (errores**2).mean()) # error cuadrático medio
# %%
ajuste_deptos.coef_ # Coeficientes
# %%
ajuste_deptos.intercept_
# %%


"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
# Fucnion que genera las primeras potencias
def pot(x,n):
    X=x.reshape(-1,1)
    for i in range(n-1):
        X=np.concatenate((X,(x**(i+2)).reshape(-1,1)),axis=1)
    return X
#--------------------------------------------------------------------
# Modelo de Akaike
def AIC(k, ecm, num_params):
# Calcula el AIC de una regresión lineal múltiple de 'num_params'
# parámetros, ajustada sobre una muestra de 'k' elementos, y que da
# lugar a un error cuadrático medio 'ecm'.
    aic = k * np.log(ecm) + 2 * num_params
    return aic
""" -----------------------------------------------------------------
-------------------------
Grado del polinomio: 1
Cantidad de parámetros: 2
ECM: 201.194
AIC: 269.213
------------------------
Grado del polinomio: 2
Cantidad de parámetros: 3
ECM: 36.325
AIC: 185.626
----------------------------------------------------------------------
Cuando complejizamos el modelo mejorando el error cuadrático medio,
pero sin disminuir el AIC, es probable que el modelo se esté
sobreajustando a los datos de entrenamiento.

Si seleccionamos el modelo ya no por su bondad de ajuste (ECM) sino
buscando el mínimo AIC ¿Qué modelo queda seleccionado? Respodé esta
pregunta usando el comando np.argmin() para encontrar el grado del
polinomio que minimiza el AIC y comentá adecuadamente tu código.
"""
#--------------------------------------------------------------------------------------------------------------
"""
Ejercicio 11.21: Gráficos de ajuste lineal con Seaborn
Seleccioná los datos correspondientes a las especies: Jacarandá, Palo borracho rosado, Eucalipto y Ceibo,
todas en un mismo DataFrame, usando el siguiente filtro.
filtro = data_arbolado_parques['nombre_com'].isin(esp_selec)
Explorá el comando de seaborn sns.regplot(), que ajusta el modelo lineal y lo grafica sin pasar por scikit
learn. El parámetro order te permite hacer ajustes polinomiales. El ci se refiere al intervalo de confianza
a sombrear.

Para facilitar la comparación que hiciste en el ejercicio anterior, graficá todos los ajustes juntos usando:

g = sns.FacetGrid(datos_selec_p, col = 'nombre_com')
g.map(sns.regplot, 'diametro', 'altura_tot')
Observación: Nos quedaron afuera de esta clase temas importantes como sobreajuste (Overfitting), partición
de los datos en conjuntos de entrenamiento y evaluación, validación cruzada, presencia de datos atípicos
(outliers), tests de hipótesis, selección de modelos... No era nuestra idea dar estos contenidos sino mostrar
un acercamiento práctico desde Python al problema de la regresión lineal.

Contenidos | Anterior (4 Práctica de Recursión) | Próximo (6 Cierre de la clase de Recursión y Regresión)
"""