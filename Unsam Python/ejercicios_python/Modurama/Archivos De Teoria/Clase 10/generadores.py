#--------------------------------------------------------------------
# %%
#
a = productor()
b = procesamiento(a)
c = consumidor(b)
# PipeLine que genera un un flujo de datos de forma ordenada ocupando
# menos memoria y mas rapido
#--------------------------------------------------------------------
# %%
#
a = [1,2,3,4]
b = tuple(2 * x for x in a)
#--------------------------------------------------------------------
# %%
#
b
#--------------------------------------------------------------------
# %%
#
for i in b:
    print(i, end=' ')

"""
El módulo itertools
El módulo itertools es una biblioteca con varias funciones útiles para construir generadores e iteradores.

itertools.chain(s1,s2)
itertools.count(n)
itertools.cycle(s)
itertools.dropwhile(predicate, s)
itertools.groupby(s)
itertools.ifilter(predicate, s)
itertools.imap(function, s1, ... sN)
itertools.repeat(s, n)
itertools.tee(s, ncopies)
itertools.izip(s1, ... , sN)
"""

