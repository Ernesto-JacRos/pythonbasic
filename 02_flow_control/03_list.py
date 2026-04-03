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