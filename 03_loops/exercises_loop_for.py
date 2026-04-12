###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
nums = list(range(2,21))
for num in nums:
    if num % 2 == 0:
        print(num, end=' ')
print() 


# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
total  = 0
for num in numeros:
    total += num
    media = total / len(numeros)
print(f'La media es: {media}')


# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
numeros = [-15, -5, -25, -10, -20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
aux = numeros[0]
for num in numeros: #recuerda que aqui es valor no el indice 
    if num > aux:
        aux = num
print(f'El numero maximo es: {aux}')


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
#Impares
#impares = [num for num in [1,2,3,4,5,6,7,8] if num % 2 != 0]
#print(impares)
# Numeros primos
print("\nEjercicio 4:")
palabras_mayores_5 = {palabra for palabra in palabras if len(palabra) > 5}
print(f'la palabras con mas de 5 letras son: {palabras_mayores_5}')
# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
letra = input('Introduce una letra: ')
contador = 0
for palabra in palabras:
    if palabra.lower().startswith(letra.lower()):
        contador += 1
print(f'El numero de palabras que empiezan con la letra {letra} es: {contador}')


