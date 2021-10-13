#--------------------------------------------------------------------
# %%
# 
import tensorflow as tf
import numpy as np
from tensorflow.python.client.pywrap_tf_session import TF_NewSessionOptions
# %%
Celsius = np.array([-40 , -10 , 0 , 8 , 15 , 22 , 38])
Fahrenheit = np.array([-40 , 14 , 32 , 46 , 59 , 72 , 100])
# %%
Capa = tf.keras.layers.Dense(units = 1 , input_shape = [1])
Modelo = tf.keras.Sequential([Capa])
# %%
Modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss =  'mean_squared_error'
)
# %%
print("Comenzando el entrenamiento")
Historial = Modelo.fit(Celsius, Fahrenheit, epochs = 1000, verbose = False)
print("Modelo entrenado")
# %%
import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de Perdida")
plt.plot(Historial.history["loss"])
# %%
print("Hagamos una prediccion")
print(Modelo.predict([100]))
# %%
print("variables internas del modelo")
print(Capa.get_weights())
# %%
#--------------------------------------------------------------------------------------------------------------
# Hacemos lo mismo pero agregamos 2 capas con 3 neuronas
#--------------------------------------------------------------------
# %%
# 
import tensorflow as tf
import numpy as np
from tensorflow.python.client.pywrap_tf_session import TF_NewSessionOptions
# %%
Celsius = np.array([-40 , -10 , 0 , 8 , 15 , 22 , 38])
Fahrenheit = np.array([-40 , 14 , 32 , 46 , 59 , 72 , 100])
# %%
# Capa = tf.keras.layers.Dense(units = 1 , input_shape = [1])
# Modelo = tf.keras.Sequential([Capa])
#--------------------------------------------------------------
Oculta1 = tf.keras.layers.Dense(units = 3 , input_shape = [1])
Oculta2 = tf.keras.layers.Dense(units = 3)
Salida = tf.keras.layers.Dense(units = 1)
Modelo = tf.keras.Sequential([Oculta1 , Oculta2 , Salida])
# %%
Modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss =  'mean_squared_error'
)
# %%
print("Comenzando el entrenamiento")
Historial = Modelo.fit(Celsius, Fahrenheit, epochs = 1000, verbose = False)
print("Modelo entrenado")
# %%
import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de Perdida")
plt.plot(Historial.history["loss"])
# %%
print("Hagamos una prediccion")
print(Modelo.predict([100]))
# %%
print("variables internas del modelo")
print(Capa.get_weights())