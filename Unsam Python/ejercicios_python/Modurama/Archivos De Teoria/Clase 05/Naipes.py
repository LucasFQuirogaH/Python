#--------------------------------------------------------------------
# %%
#
import random
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]
carta = random.samples(naipes , k = 1)
#--------------------------------------------------------------------
# %%
#
import numpy as np
a = np.array([[1 , 2 , 3 , 4], [5 , 6 , 7 , 8], [9 , 10 , 11 , 12]])
# %%
a
# %%
a[2]
# %%
import numpy as np
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
# %%
arr
# %%
arrord = np.sort(arr)
# %%
arr
# %%
arrord
# %%
id(arrord) == id(arr)
#--------------------------------------------------------------------
# %%
#
import numpy as np
arreglo = np.array([1 , 2 , 3 , 4])
# %%
print(np.nonzero(arreglo >= 3))
# %%
