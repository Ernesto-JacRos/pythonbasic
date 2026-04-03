###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

import os
os.system('cls')

number_one = input('introduce el primer numero: ')
number_two = input('introduce el segundo numero: ')
if number_one > number_two:
    print(f'{number_one} es mayor que {number_two}')
elif number_one < number_two:
    print(f'numero {number_two} es mayor que {number_one}')
else:
    print(f'{number_one} es igual a {number_two}')

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

uno = int(input('introduce el primer valor: '))
dos = int(input('introducd el segundo valor: '))

operacion = input('introduce el tipo de operacion: \n* multiplicacion\n/ division, \n+ suma\n- resta\n')
if operacion == '*':
    print(uno * dos)
elif operacion == '/':
    if dos == 0:
        print('Error, no s epude dividir entre cero')
    else:
        print(uno / dos)
elif operacion == '+':
    print(uno + dos)
elif operacion == '-':
    print(uno - dos)
else:
    print('La operacion es invalidad')

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.
print('escribe el anho para saber si es bisiesto')
year = int(input('escribe el anho a confrimar:  '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('es anho bisiesto')
else:
    print('No es anho bisiesto')

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input('introduce tu edad:  '))
if 0 <= edad <= 2: 
    print('bebe')
elif 3 <= edad <= 12:
    print('ninho')
elif 13 <= edad <= 17:
    print('adolescente')
elif 18 <= edad <= 64:
    print('Adulto')
elif edad >= 65:
    print('Adulto mayor')
else: 
    print('Edad invalida')