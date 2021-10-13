"""------------------------------------------------------------------------------------------------------------
Examen Final.
Ing.Lucas F. Quiroga H. Fecha: 24/06/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 15:10:41 2021

@author: flacus
"""
# %%
#
class Lote:
	def __init__(self, f, c, p):
		self.nombre = f
		self.cajones = c
		self.precio = p

	def __repr__(self):
		return f'Lote({self.nombre}, {self.cajones}, {self.precio})'

	def __str__(self):
		return f'Lote: {repr(self.nombre)} / {self.cajones} / ${self.precio}'

	def costo(self):
		return self.cajones * self.precio

	def vender(self, n):
		self.cajones -= n

#%%
#Porque no obtengo la misma salida si ejecuto print(milote)
#que si pido el valor de milote ?
"""------------------------------------------------------------------------------------------------------------
Respuesta: Cuando se definen los metodos __str__ y __repr__ dentro de una clase se hace con el proposito de
brindar una mejor vista para el operador y/o programador. Son metodos especiales. __str__ muestra el formato
definido en el mismo metodo, y respectivamente __rep__ mostrara su formato al ejecutar por consola miLote.
__repr__ indica que debe devolver un string para que cuando pase por eval() cree el objeto.
En ambos casos y sin tener esos metodos definidos tendremos las siguientes salidas por consola respectivamente.
<__main__.Lote object at 0x00000242A23C2FA0>
<__main__.Lote at 0x1b633fb20a0>
------------------------------------------------------------------------------------------------------------"""

#--------------------------------------------------------------------
# %%
#
milote = Lote("naranja" , 100, 32.2)
print(milote)
#--------------------------------------------------------------------
# %%
#
milote
#--------------------------------------------------------------------
"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""
# %%
#
def iterador(n):
	for i in range (n):
		if i//2 == i/2:
			yield i
#--------------------------------------------------------------------
pares = iterador(10)
#--------------------------------------------------------------------
#%%
#Porqué el iterador "pares" devuelve 5 elementos, y no tantos como le pida ?
"""------------------------------------------------------------------------------------------------------------
Respuesta: Dentro de la funcion, en la linea if i//2 == i/2: se observa que esa condicion es valida cada vez
que i corresponde a un numero par, por lo que solo devolvera los pares, sin contar el 10 ya que el rango de for
llega hasta 9.
------------------------------------------------------------------------------------------------------------"""
#--------------------------------------------------------------------
# %%
#
for elemento in pares: print(elemento)
#--------------------------------------------------------------------
# %%

"""------------------------------------------------------------------------------------------------------------
S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O R  S E P A R A D O
------------------------------------------------------------------------------------------------------------"""

#%%
# Porqué es mas eficiente usar una variante de ordenamiento por Seleccion que una variante de Merge Sort
# en este caso hipotético ?

# Dada una secuencia de enteros S, se quiere implementar una estrategia para ubicar en el lugar correcto
# (en términos de ordenamiento ascendente) los K mayores elementos de S, donde K es significativamente
# menor que len(S). Para fijar ideas, digamos que S tiene mil millones de elementos y que K=12.

"""------------------------------------------------------------------------------------------------------------
Respuesta: El metodo de ordenamiento por seleccion se basa en encontrar el maximo y llevarlo al final de la
lista. Luego en la proxima vuelta, se buscara  hasta n - 1, el proximo mayor, porque el ultimo esta en la
posicion correcta.
Por lo tanto los k mayores de la lista seran los primeros en ser ordenados y ubicados en las ultimas posiciones.
De hecho asi es el metodo.
------------------------------------------------------------------------------------------------------------"""