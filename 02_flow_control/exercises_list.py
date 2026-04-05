
import os 
os.system('cls')
###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.
lista_numeross = [1, 2, 3, 4, 5]
lista_numeross.append(6)
print(lista_numeross)
lista_numeross.insert(2, 10)
print(lista_numeross)
lista_numeross[0] = 0
print(lista_numeross) 

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
print(lista_a)
lista_a.remove(1)
print(lista_a)
elemento_eiminado = lista_a.pop(3)
print(lista_a)
print('Elemento eliminado = ', elemento_eiminado)
lista_b.clear()
print(lista_b)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista_numeros[2:5]
print(lista_numeros)

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.
print('Ejrcicio # 4')
numeros_ejercico = [5, 2, 8, 1, 9, 4, 2]
print(numeros_ejercico)
numeros_ejercico.sort()
print(numeros_ejercico)
print(numeros_ejercico.count(2))
print('Esta el # 7 en numero: ',7 in numeros_ejercico)

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

numeros_ejercico5 = [1, 2, 3]
numeros_ejercico5_copia = numeros_ejercico5[:]
print(numeros_ejercico5_copia)
copia2 = numeros_ejercico5.copy()
print(copia2)
referencia = numeros_ejercico5
referencia.insert(0,10)
print('i,resion de las listas')
print('origina: ', numeros_ejercico5)
print('copia con slicing; ', numeros_ejercico5_copia)
print('copia con metodo copy(): ', copia2)
print('Referecia:  ', referencia)


# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.
lista_frutas = ["Manzana", "pera", "BANANA", "naranja"]
lista_frutas.sort(key=str.lower)
print(lista_frutas)