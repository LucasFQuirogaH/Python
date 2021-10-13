"""--------------------------------------------------------------------------------------------------------------------------------------------------
Probamos codigo de otros
--------------------------------------------------------------------------------------------------------------------------------------------------"""
# def propagar_al_vecino(l):
#     modif = False
#     n = len(l)
#     for i,e in enumerate(l):
#         if e==1 and i<n-1 and l[i+1]==0:
#             l[i+1] = 1
#             modif = True
#         if e==1 and i>0 and l[i-1]==0:
#             l[i-1] = 1
#             modif = True
#     return modif

# def propagar(l):
#     m = l.copy()
#     veces=0
#     while propagar_al_vecino(l):
#         veces += 1

#     print(f"Repetí {veces} veces la función propagar_al_vecino.")
#     print(f"Con input {m}")    
#     print(f"Y obtuve  {l}")
#     return m
# #%%
# propagar([0,0,0,0,1])
# propagar([0,0,1,0,0])
# propagar([1,0,0,0,0])
# %%
"""--------------------------------------------------------------------------------------------------------------------------------------------------
Preguntas:
¿Por qué los tests l[i+1]==0 y l[i-1]==0 de la función propagar_al_vecino no causan un IndexError en los bordes de la lista?
¿Por qué propagar([0,0,0,0,1]) y propagar([1,0,0,0,0]), siendo entradas perfectamente simétricas, no generan la misma cantidad
de repeticiones de llamadas a la función propagar_al_vecino? # PORQUE AL IR HACIA ADELANTE VA ENCENDIENDO EL SIGUIENTE EN LA MISMA LLAMADA.
EN LA ANTERIOR POR CADA VEZ QUE TERMINA HAY QUE REINICAR LA LLAMADA PORQUE ATRAS QUEDARON FOSFOROS SIN ENCENDER.
Sobre la complejidad. Si te sale, calculá:
¿Cuántas veces como máximo se puede repetir el ciclo while en una lista de largo n? N + 1
¿Cuántas operaciones hace "propagar_al_vecino" en una lista de largo n? N + CANTIDAD DE OPERACIONES EXTRAS COMO ASIGNACIONES
Entonces, ¿cuántas operaciones hace como máximo esta versión de propagar en una lista de largo n? ¿Es un algoritmo de
complejidad lineal o cuadrática? LINEAL
--------------------------------------------------------------------------------------------------------------------------------------------------"""
#%%
def propagar_a_derecha(l):
    n = len(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1:
            if l[i+1]==0:
                l[i+1] = 1
    return l
#%%
def propagar(l):
    ld=propagar_a_derecha(l)
    lp=propagar_a_izquierda(ld)
    return lp
#%%
l = [0,0,0,-1,1,0,0,0,-1,0,1,0,0]
print("Estado original:  ",l)
print("Porpagando...")
lp=propagar(l)
print("Estado original:  ",l)
print("Estado propagado: ",lp)

"""--------------------------------------------------------------------------------------------------------------------------------------------------
Preguntas:
¿Por qué se modificó la lista original?
¿Por qué no quedó igual al estado propagado?
Corregí el código para que no cambie la lista de entrada.
¿Cuántas operaciones hace como máximo propagar_a_derecha en una lista de largo n?
Sabiendo que invertir una lista ([::-1]) requiere una cantidad lineal de operaciones
en la longitud de la lista ¿Cuántas operaciones hace como máximo propagar en una lista de largo n?
--------------------------------------------------------------------------------------------------------------------------------------------------"""
# %%
