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


