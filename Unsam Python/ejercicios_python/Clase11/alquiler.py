#--------------------------------------------------------------------
# %%
#
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
# %%
modelo= linear_model.LinearRegression()
modelo.fit(superficie.reshape(-1 , 1) , alquiler)
# %%
a = modelo.coef_[0]
b = modelo.intercept_
print(a , b)
# %%
errores = alquiler - (a * superficie + b)
print(errores)
print("ECM:", (errores**2).mean())
# %%
L = np.array([0 , 200])
plt.scatter(superficie , alquiler)
plt.plot(superficie , alquiler , c = 'g' , label = 'Realidad')
plt.plot(L , a*L + b , c = 'r' , linestyle = '-.' , label = 'Modelo')
plt.legend()
# %%
