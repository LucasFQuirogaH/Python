"""------------------------------------------------------------------------------------------------------------
Geringoso
Ing.Lucas F. Quiroga H. Fecha: 15/11/2021 Retroceder nunca, rendirse jamas
------------------------------------------------------------------------------------------------------------"""
# Import ------------------------------------------------------------------------------------------------------
# %%
# Funciones ---------------------------------------------------------------------------------------------------
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def ShowGerin(Woord):
#Contrato:
# Precondicion:
# Poscondicion:
    print(f"{Woord}")
    return None
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def TrasformerGerin(Word):
#Contrato:
# Precondicion:
# Poscondicion:
    Woord = ""
    for c in Word:
        if c == "a":
            Woord = Woord + "apa"
        elif c == "e":
            Woord = Woord + "epe"
        elif c == "i":
            Woord = Woord + "ipi"
        elif c == "o":
            Woord = Woord + "opo"
        elif c == "u":
            Woord = Woord + "upu"
        else:
            Woord = Woord + c
    ShowGerin(Woord)
    return None
## Funciones: Busqueda lineal ---------------------------------------------------------------------------------
# %%
def GetWord():
#Contrato:
# Precondicion:
# Poscondicion:
    Word = input("Ingrese la palabra para transformar a geringoso: ")
    TrasformerGerin(Word)
    return None
## Funciones: Funcion principal Main --------------------------------------------------------------------------
# %%
def main():
# El main como programa principal
    GetWord()
    return None

# Main  -------------------------------------------------------------------------------------------------------
# %%
if __name__ == '__main__':
    main()