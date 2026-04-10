###
# 01 - Bucle (while)
# permitebe ejecutar un bloque de código mientras se cumpla una condición
###
print('Bucle while')
# Bucle while simple
contador = 0
while contador <= 5:
    print('Contador:', contador)
    contador += 1 # Incrementamos el contador para evitar un bucle infinito

# Utilizando la paabra break para romper un bucle
print('\nBucle while con break')
contador = 0 
while True: #Bucle infinito
    print('Contador:', contador)
    contador += 1
    if contador > 5:
        break # Rompe el bucle cuando el contador es mayor a 5

# se usa break para casos donde no sabes que eemento vas a encontrar ni en que momento,
# por ejemplo al leer un archivo hasta encontrar una palabra clave o al esperar una entrada del
# usuario hasta que se ingrese un valor específico. 
# o que encuenres el primer valor que cumpla con la condición que estas buscando.

print('Bucle while que encuentra el primer número que cumple una condición')
contador = 0
while contador <=100:
    contador += 1
    print(contador)
    if contador % 5 == 0:
        print('El primer número que es múltiplo de 5 es:', contador)
        break

# Continue en bucles while
#continue, salta esa iteracion en concreto 
#y cintinua con el bucle, es decir, con la siguiente iteración.
print('\nBucle while con continue')
# salta los números pares y solo imprime los impares
contador   = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0: #se salta esta iteracion 
        continue
    print(contador)
#podemos filtar si tenemos una lista de elementos y queremos imprimir solo los que cumplen una condición
# si un usuario tiene ciertos privilegios, etc. 

# else en while
print('\nBuvle while con else')
contador = 0
while contador < 5:
    print('Contador:', contador)
    contador += 1
else:
    print('El bucle ha terminado')#cuando la condicon del bucle ha terminado 
# Caso especial donde no se llega al else porque se rompe el bucle con break
# Entoces lo puedes usar para asegurar que el bucle ha termiando normalmente sin interrupciones.

# Pedirle al usuario un numero que debe ser positivo si no no lo dejas en paz 
numero = -1 
while numero <= 0:
    numero = int(input('Escribe un numero positivo: '))
    if numero < 0:
        print('E numero debe ser positovo, intenta de nuevo ')


print(f'el nuemro introducido es: {numero}')
