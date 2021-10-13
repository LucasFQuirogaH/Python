# """
# Diccionario: Un tipo de datos que alamcena un conjunto de datos en formato clave y valor.
# Es parecido a un array asociativo o un objero json
# """

persona ={
    "nombre" : "Lucas" ,
    "apellido" : "Quiroga" ,
    "correo" : "lucquifer@hotmail.com"
    
}

# print(persona["apellido"])


contactos = [
    {
        "nombre" : "Lucas Quiroga" ,
        "email" : "lucquifer@hotmail.com" ,
    } ,
    
    {
        "nombre" : "Antonio Fragale" ,
        "email" : "fragale10@gmail.com"
    }
    
]

#print (contactos[0]["email"])
print("\n")
for indice in contactos :
    print(f"Nombre: {indice['nombre']}")
    print(f"Correo: {indice['email']}")
    print("--------------------------------")
