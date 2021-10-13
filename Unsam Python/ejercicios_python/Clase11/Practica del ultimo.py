#--------------------------------------------------------------------
# %%
#
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import argmax
import pandas as pd
from sklearn import linear_model
import numpy as np
#--------------------------------------------------------------------
# %%
#
x = np.random.uniform(0 , 10 , 25)
y = 2 * x - 8
# plt.scatter(x , y)
plt.hist(x , bins = 15)
# %%
N = 100
x = np.random.uniform(0 , 10 , N)
r = np.random.normal(0 , 1 , N)
y = 2 * x - 8 + r
# plt.scatter(x , y)
plt.plot(x , 2 * x - 8 , c ='g')
#--------------------------------------------------------------------
# %%
#
modelo= linear_model.LinearRegression()
modelo.fit(x.reshape(-1 , 1) , y)
# %%
a = modelo.coef_[0]
b = modelo.intercept_
print(a , b)
#--------------------------------------------------------------------
# %%
#
L = np.array([0 , 10])
plt.scatter(x , y)
plt.plot(L , 2 * L - 8 , c = 'g' , label = 'realidad')
plt.plot(L , a*L + b , c = 'r' , linestyle = '-.' , label = 'Moledo')
plt.legend()
# %%
L = np.array([0 , 10])
ysombrero = a * x + b
plt.scatter(x , ysombrero , c = 'g' , label = r'$\hat{y}$')
plt.scatter(x , y , c = 'b' , label = 'y')

plt.plot(L , a * L + b , c = 'r' , linestyle = '-.' , label = 'Modelo')
for i , d in enumerate(x):
    if i == 0:
        plt.plot([d , d] , [y[i] , ysombrero[i]] , c = 'b' , label = 'residuos')
    else:
        plt.plot([d , d] , [y[i] , ysombrero[i]] , c = 'b')
plt.legend()
# %% Grafico de verosimilitud
from scipy.stats import norm
pesos = np.array([960.0 , 1035.0 , 1002.0])
mus = np.linspace(960 , 1100 , 141)
verosi = np.ones(len(mus))
sigma = 10
for i , mu in enumerate(mus):
    for p in pesos:
        verosi[i] *= norm.pdf(p , mu , sigma)
plt.plot(mus , verosi)
# %%
# Grafico del logaritmo. Aquise puede derivar mas facil y encontrar un maximo
plt.plot(mus , np.log(verosi))
# %%
# Le pedimos que de el numero que corresponde al peso mas verosimil
mus[np.argmax(verosi)]
# %%
# Si haces el promedio
pesos.mean()
# %%
