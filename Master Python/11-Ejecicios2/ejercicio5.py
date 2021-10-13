"""-------------------------------------------------------------------------------------------------------------------
Crear una lista con el ejercicio de una tabla:
ACCION                  AVENTURA                  DEPORTE
GTA                     ASSINS                    FIFA 21
COD                      CRASH                     PRO 21
PUGB                PRINCE OF PERSIA             MOTO GP 21
Guardar en diccionario. Mostrar la informacion ordenada.
Mostrar por categoria.
-------------------------------------------------------------------------------------------------------------------"""

#Main------------------------------------------------------------------------------------------------------------------

tabla = [
    {
        "categoria" : "ACCION" ,
        "juegos" : ["GTA" , "COD" , "PUGB"]
    } , 
    {
        "categoria" : "AVENTURA" ,
        "juegos" : ["ASSINS" , "CRASH" , "PRINCE OF PERSIA"]
    } ,
    {
        "categoria" : "DEPORTE" ,
        "juegos" : ["FIFA 21" , "PRO 21" , "MOTO GP 21"]
    }
]

for categoria in tabla :
    print(f"------------{categoria['categoria']}------------")
    for juegos in categoria['juegos'] :
        print(juegos)
