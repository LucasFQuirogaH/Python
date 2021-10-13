# def tiene_a(expresion)
#     import traceback
#     n = len(expresion)
#     i = 0
#     while i<n
#         if expresion[i] = 'a'
#             return True
#         i += 1
#     return Falso

# import traceback
# tiene_a('UNSAM 2020')
# tiene_a('La novela 1984 de George Orwell')
# format_exc()

# import csv
# with open("Data/camion.csv" , "r" , encoding="utf8") as Creacion:
#     Lectura = list(csv.reader(Creacion))
#     print(Lectura)

# nombre = "Naraja"
# cajones = 100
# precio = 32.20
# print(f"{nombre:>10s} {cajones:>10d} {precio:>10.2f}")

# s={
#     "nombre" : "Naranja",
#     "cajones" : 100,
#     "precio" : 32.20
# }
# print("{nombre:>10s} {cajones:>10d} {precio:>10.2f}".format_map(s))

# value = 42863.1
# print(value)

# # Con 4 decimales flotante
# print(f"{value:0.4f}")

# # 16 lugares a la derecha con 2 decimales
# print(f"{value:>16.2f}")

# # 16 lugares a la izquierda con 2 decimales
# print(f"{value:<16.2f}")

# # 16 lugares a la izquierda con 2 decimales y rellena con asteriscos
# print(f"{value:*>16,.2f}")

# value = "%0.4f"
# print(value)


# cadena="var1"
# valor="casa"
 
# exec(cadena + " = ' "+valor+" '")
 
# print(var1)

#--------------------------------------------------
# x='buffalo'
# exec("%s = %d" % (x,2))
# print(buffalo)

#--------------------------------------------------
# x='buffalo'
# vars()[x] = "Hola"
# print(buffalo)
#--------------------------------------------------

# auxiliar =""
# Headers = ("Nombre" , "Cajones" , "Precios" , "Cambio")
# for elemento in list(Headers):
#     auxiliar = elemento
#     vars()[auxiliar] = elemento # Nombre = "Nombre" 
# print (Nombre)
# print (Cajones)
# print (Precios)
# print (Cambio)

# import csv
# from collections import Counter
# tenencias = Counter()
# UnDiccionario = {}
# with open("Data/camion.csv" , "r" , encoding="utf8") as Creacion:
#     Lectura = csv.reader(Creacion)
#     cabecera = next(Lectura)
#     for Linea in Lectura:
#         UnDiccionario = dict(zip(cabecera, Linea))
#         tenencias[UnDiccionario["nombre"]] += int(UnDiccionario["cajones"])
# print(tenencias)

citricos = { 'Naranja','Limon','Mandarina' }
# Alternativamente podemos escribirlo así:
citricos = set(['Naranja', 'Limon', 'Mandarina'])

juan= 'Naranja' in citricos
print(juan)
