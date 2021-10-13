# Es un tipo de datos para tener una coleccion de valores pero sin orden ni indice

personas = {
    "Victor" , 
    "Manolete" , 
    "Francisco"
}
print(personas)
print(type(personas))

personas.add("Mariana")
print(personas)

personas.remove("Francisco")
print(personas)