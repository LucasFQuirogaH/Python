cantantes = ['bad bunny' , 'daddy yankee' , 'Luis Fonsi']
numeros = [1 , 2 , 8 , 6 , 3 , 7 , 9]

# print (numeros)
# numeros.sort()
# print(numeros)

cantantes.insert( 1 , "maluma")
print(cantantes)

cantantes.pop( 3 )
print(cantantes)

cantantes.remove('maluma')
print(cantantes)

numeros.reverse()
print(numeros)

print('daddy yankee' in cantantes)
print(len(cantantes))

numeros.append(9)
numeros.append(9)
print(numeros.count(9)) 

