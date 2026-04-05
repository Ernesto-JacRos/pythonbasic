###
# 04 - Listas Methods
# Los metodos mas importantes para trabajar con listas
###

import os
os.system('cls')
listas_enteros = [1, 2, 3, 4, 5]

#Agregar o Insertar elementos a la lista

# Agregar un elemento a una lista al final
listas_enteros.append(6)#anhade un elemento al final de la lista 
print(listas_enteros)

# Inserta un elemento en la posicion que le indiquemos que es el primier parametro del method insert()

lista_str = ['a', 'b', 'c', 'e', 'f']
lista_str.insert(1, '@')#primer arguemnto el indice y 2do el valor que queremos agregar
print(lista_str)

# Agregar uno o mas elementos al final de la lista method extend()
lista_str.extend(['Ernesto', 'Jacros', 'Dev'])
print(lista_str)

# Eliminar elementos de la lista 

#Elimina el primer elemento que coincida con el argumento del method remove()
lista_str.remove('@')
print(lista_str)# no se pasa indices, sino el elemento que que se desea borra

# Eliminar el ultimo de la lista
eliminado = lista_str.pop() # te devuelve el elemento borrado
print(lista_str)
print('Elemento eliminado: ', eliminado) #defecto tiene el indice -1 que ya sabemos que es el ultimo

# y puedes pasar cualqueir indice que desees elieminar
elemento_eliminado = lista_str.pop(1)
print('Elemento eliminado: ', elemento_eliminado)
print(lista_str)

# Eliminar con otra sintaxis
# Puedes eliminar un rango de elementos
del lista_str[0]## se pasa le indice 
print('usando del')
print(lista_str)

# Eliminar todos los elementos de la lista 

lista_str.clear()
print('Usando Clear()')
print(lista_str)

# Usando del para borrar rangos

lista_str = ['a', 'b', 'c', 'd', 'e', 'f']
print(lista_str)
del  lista_str[1:3] 
print(lista_str)