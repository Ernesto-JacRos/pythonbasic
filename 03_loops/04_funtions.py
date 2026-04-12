import os
os.system('cls')
###
# 04 - Funciones 
# Bloque de codigo reutilizable y parametrizables para hace run codigo 
# para tareas especifiocas
####
'''Definicion de una funcion 
def nombre_de_la_funcion(parametro1, parametro2):
    #docstring (opcional)
    #cuerpo de la funcion
    return resultado (opcional)
''' 
#Ejemplo funcion mas basica 
def saludar():
    print('Hola, bienvenido a mi programa')

saludar()

def saludar_nombre(nombre):
    print(f'Hola, {nombre}')

saludar_nombre('Jacros')
saludar_nombre('Maria')
saludar_nombre('Pedro')
saludar_nombre('Ana')
# El parametro es lo que acepta la funsion para realizar su tarea, el argumento es el valor que se le asigna a ese parametro al momento de llamar a la funcion
# Parametro es cuando se define la funcion, argumento es cuando se llama a la funcion
def suma(a,b):
    resultado = a + b
    return resultado

print('Resultado de suma: ',suma(3,5))

# Documentar las funcines con docstrig 
def resta(a:int,b: int)-> int:
    '''Esta funcion realiza la resta de dos numeros'''
    return a - b

print('Resultado de resta: ',resta(10.5,4.2))
print(resta.__doc__)# acceder a la documentacion de la funcion con __doc__

#puedes usar hepl para acceder a la documentacion de la funcion
help(resta)

# Parametros por defecto 
def multiplicar(a:int , b:int=2) -> int:
    '''Esta funcion multiplica dos numeros, el segundo parametro tiene un valor por defecto de 2'''
    return a * b

print('Resultado de multiplicar: ',multiplicar(5)) # el segundo parametro toma el valor por defecto de 2
print('Resultado de multiplicar: ',multiplicar(5,3)) # el segundo parametro toma el valor de 3

# Paramtros por posicion y por nombre
# es como parametros nombrados de kotlin
def person_descritption(nombre:str, edad:int, ciudad:str) -> str:
    '''Esta funcion recibe el nombre, edad y ciudad de una persona y devuelve una descripcion'''
    return f'{nombre} tiene {edad} años y vive en {ciudad}'

print(person_descritption('Jacros', 30, 'Madrid')) # parametros por posicion
print(person_descritption(edad = 30, ciudad = 'CDMX', nombre  = 'Jacros')) # parametros por nombre

# Argumenttos d elonguitud variable
def suma_variables(*args):
    '''Esta funcion recibe una cantidad variable de argumentos y devuelve la suma de ellos'''
    resultado = 0
    for num in args:
        resultado += num
    return resultado

print('Resultado de suma_variables: ', suma_variables(1, 2, 3, 4, 5))
print('Resultado de suma_variables: ', suma_variables(10, 20, 30))
print('Resultado de suma_variables: ', suma_variables(5, 10, 15, 20, 25, 30))

# Argumentos de clave - valor variable(**kwargs)

def monstrar_info_person(**kwargs):
    '''Esta funcion recibe una cantidad variable de argumentos de clave - valor 
    y muestra la informacion de una persona'''
    for key, value in kwargs.items():
        print(f'{key}: {value}')
print('Informacion de la persona: ')
monstrar_info_person(nombre = 'Jacros', edad = 30, ciudad = 'Madrid')
print()
monstrar_info_person(nombre = 'Maria', edad = 25, ciudad = 'CDMX', profesion = 'Ingeniera')
print()
monstrar_info_person(nombre = 'Pedro', edad = 40, ciudad = 'Barcelona', profesion = 'Doctor', hobby = 'Futbol')
print()