#--------------------------------------------------------------------
# %%
# Factorial
def factorial(n):
# Precondición: n entero positivo
# Devuelve: n!
    if n == 1:
        return 1
    if n == 0:
        return 1
    return n * factorial(n - 1)
#--------------------------------------------------------------------
# %%
#
factorial(1)
factorial(3)
factorial(4)
factorial(0)
# %%
factorial(9)
# %%

