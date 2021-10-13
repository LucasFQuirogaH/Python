# %%
def pascal(n , k):
    if n == 0:
        res = 1
    elif k == 0:
        res = 1
    elif k == n:
        res = 1
    else:
        res = pascal(n - 1 , k - 1) + pascal(n - 1 , k)
    return res
#--------------------------------------------------------------------
# %%
#
pascal (5 , 3)
# %%
