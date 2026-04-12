###
# 02 - Bucles (for)
# Permite ejecutar un bloque de codigo repetidamente mientras ITERA un iterable o una lista
###

print('\nBucle for')
#Ietrar una lista 
frutas = ['manzana', 'pera', 'mandarina']

for fruta in frutas:
    print(fruta)

# Iterar sobre cualqueir cosa que sea iterable
cadena = 'jacrosdev'
for letra in cadena:
    print(letra, end=' ')

# enumerae()  para obtener indices y valores al mismo tiempo
print('\nEnumerate')
frutas = ['manzana', 'pera', 'mandarina', 'uva', 'fresa', 'durazno']
for index, fruta in enumerate(frutas):
    print(f'el indice es: {index} y la fruta es: {fruta}')

# Bucles anidades

letras = ['a', 'b', 'c']
numeros = [1, 2, 3]
for letra in letras:
    for numero in numeros:
        print(f'{letra} x {numero}')

n = 4
for i in range(n):
    espacios =  n - i - 1
    estrellas = 2 * i + 1
    print(' '  * espacios + '*' * estrellas)

# Break eb for 

animales = ['perro', 'gatos', 'pez', 'pajaro', 'caonejo', 'hamster']

for idx, animal in enumerate(animales): 
    print(animal)
    if animal  == 'pez':
     print(f'ya lo encontre, el lo se encoden enmero {idx}')
    break


print('pez' in animales)    

# Continue 
animales = ['perro', 'gatos', 'pez', 'pajaro', 'caonejo', 'hamster']
for idx, animal in enumerate(animales): 
    if animal  == 'pez':
     continue
    print(animal, end=' ')
    print()

#Compresion de listas (list comprehensions)
animales = ['perro', 'gatos', 'pez', 'pajaro', 'caonejo', 'hamster']
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# compresion de listas con if

pares = [num for num in [1,2,3,4,5,6,7,8] if num % 2 == 0]
print(pares)

#Impares
impares = [num for num in [1,2,3,4,5,6,7,8] if num % 2 != 0]
print(impares)
# Numeros primos