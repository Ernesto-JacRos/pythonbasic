###
# 03 - Listas
# Secuencias mutables de elementos
# Pueden contener elementes de diferentes tipos.
###
import os
os.system('cls')
#Creacion de Listas 
print('\nCrear Listas')
lista_enteros: list[int] = [1, 2, 3, 4, 5] #Lsitas de enteros
list_str = ['Manzanas', 'Peras', 'Platanos'] #lista strs
list_mix: list[int | str | float | bool] = [1, 'hola', 3.14, True] #Lista Mixtos
#Lista Vacia
lista_vacia = []
#listas de listas
listas_de_listas = [[1,2], [3,4]]
#Matriz
matrix = [[1,2], [2,3], [4,5]]
print(list_str)
print(lista_enteros)
print(list_mix)
print(lista_vacia)
print(listas_de_listas)
print(matrix)

# Acceder a elementos spor indice
print('Aceeder a elementos por indice')

print(list_str[0]) # Manzanas
print(list_str[1]) # Peras
print(list_str[2]) # Platanos

##si queremos acceder al ultimo elemento podemos acceder con indice negativo
print(list_str[-1]) # platanos 
print(list_str[-2]) # Peras
print(list_str[-3]) # Manzabass

# Acceder a listas de listas
print('Impresion de listas')
print(listas_de_listas)
print(listas_de_listas[1][0]) #1 que es el segundo item de la lista y 0 que es el primer elemento de la lsita interna

#Slicing (rebanado) de listas
print('Slicing ')
lista_enteros: list[int] = [1, 2, 3, 4, 5]
print(lista_enteros[1:4])# [2, 3, 4] no cuenta el ultimo indice  no incluyente

#tener los primeros 3
print(lista_enteros[:3] )

# o de tal indice hasta el final 
print(lista_enteros[3:]) 

#para hacer una copia 
print(lista_enteros[:])

# hace una copia desde hasta (no incluyente) y tercer paramettro el paso 
lista_enteros: list[int] = [1, 2, 3, 4, 5,6, 7, 8]#[1, 2, 3, 4, 5]
print(lista_enteros[::2])

#copia de inicio hasta el final; pero inversa 
print(lista_enteros[::-1])

#Modificar elementos de la lista 
lista_enteros[0] = 20
print(lista_enteros) 

# Anhadier elementos a una lista
# primera forma 
lista_enteros = lista_enteros + [10, 11, 12]
print(lista_enteros)
# Froma ma corta y efeciente
lista_enteros += [13, 14, 15]
print(lista_enteros)

# Recuperar longittud de la lista 

print('Longitud de la lista: ', len(lista_enteros))

# Ordenar Lista en python 
print('Ordenar listas modificando la original ')
#sort() no devuelve nada y por eso modifica internamente la listra
numbers = [2,4,6,8,3435,23,-1,0]
print(numbers)
numbers.sort()
print(numbers)

print('Ordenar listas creando un original')
# devuelve una lista (la copia ) y conservas la original
#el metodo la devuelve y la puede guardar en un avariable
numbers = [2,4,6,8,3435,23,-1,0]
lista_ordenada = sorted(numbers)
print(numbers)
print(lista_ordenada)

# Odenar Cadenas de texto
print("Odenar cadenas de texto todo en nimusculas")

lista_str = ['manzana', 'pera', 'limon', 'manzana', 'pera','limon']
frutas_ordenadad = sorted(lista_str)
print(frutas_ordenadad)

print('Comparacion con mayuscula y minusculas')
print('tiene un orden distinto porque ordena po mayusculas ')
lista_str = ['manzana', 'Pera', 'Limon', 'manzana', 'pera','limon']
mix_frutas = sorted(lista_str)
print(mix_frutas)
print()
print('se hace la comparacion pero todas tomadas como minusculas')
# Se hace con sort un que la comparacion se hace con lowercase, 
# no modifica la cadena en si 
print()
mix_frutas.sort(key=str.lower)
print(mix_frutas)
print()

#Mas metodos

lista_enteros: list[int] = [1, 2, 3, 4, 5,6, 7, 8, 1,1]#[1, 2, 3, 4, 5]

print('Tamanho de la lista ', len(lista_enteros)) ##Tamanho de la lista
print('Cuantas veces aparace el 1 en lista enteros: ', lista_enteros.count(1)) ##Cuantas veces aparace el elemento 
##para saber si un elemento esta dentro de la lista 
print(1 in lista_enteros)## devuelve un booleao 

