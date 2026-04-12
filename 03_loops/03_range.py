###
# 03 - range()
# Permite crear una secuencia de numeros, puede ser util para for 
###
import os
os.system('cls')
print('\nRange')
nums = range(5) # no crea una lista 
print(type(nums))# Type range
print(nums)
# rango no crea una lista en si, va va creando bajo demanda 
# por defecto el inico en 0
# Generando una secuencia del 0 al 9 
for num in range(10):
    print(num, end=' ')
print()

# range(inicio , fin )
for num in range(5,10):
    print(num, end=' ')
print()

# rango(inicio, fin, step)

for i in range(0,20,2):
    print(i,end=' ')
print()

# numeros negativos 
for i in range(-5, 0):
    print(i, end=' ')
print()
#decrementando el valor 
for i  in range(10, 0, -1):
    print(i, end=' ')
print()
# range no crea una lista , crea los numeros sobre la marcha 

#para crear una lista a partie de un rabge() usas el merhod list()
nums = range(5)
nums_list = list(nums)
print(nums_list)


# uso de range() para repetir acciones 
for _ in range(5):
    print('Hola')

