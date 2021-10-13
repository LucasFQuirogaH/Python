#--------------------------------------------------------------------
# %%
#
def hojas(n):
    if n == 0:
        LargoEneMenos1 = 1189
        AnchoEneMenos1 = 841
    else:
        LargoEne , AnchoEne = hojas(n - 1)
        LargoEneMenos1 = AnchoEne
        AnchoEneMenos1 = LargoEne // 2
    return LargoEneMenos1 , AnchoEneMenos1
#--------------------------------------------------------------------
# %%
#
print(hojas(4))