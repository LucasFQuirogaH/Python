# Coelcciones de datos ajo un unico nombre

peliculas = ["batman" , "spiderman" , "El señor de los anillos"]

cantantes = list (('Rolling Stones' , 'Jenifer Lopez'))

#print(peliculas[-2])

cantantes.append ("Alejandro Fernandez")

# print (cantantes)

# for indice in peliculas :
#     print (indice)

# for indice in peliculas :
#     print (f"{peliculas.index(indice)}.{indice}")

# nuevaPelicula =""
# nuevaPelicula = input ("Ingrese una nueva pelicula al listado: ")
# while nuevaPelicula != "parar" :
#     peliculas.append(nuevaPelicula)
#     nuevaPelicula = input ("Ingrese una nueva pelicula al listado: ")

# for indice in peliculas :
#     print (f"{peliculas.index(indice)}.{indice}")

#-----------------------------------------------   Ejemplo 2 ---------------------------------------------------

contactos = [
    [
        'Lucas Quiroga' ,
        'lucquifer@hotmail.com'
 
    ] ,

    [
        'Marcela Fragale' ,
        'marcelafragale@hotmail.com'
 
    ] ,
    
    [
        'Antonio Fragale' ,
        'fragale10@Gmail.com'
 
    ]
]

# print(contactos[2][1])

for lista1 in contactos :
    print("\n")
    # print (lista1)
    for lista2 in lista1 :
        print(lista2)
