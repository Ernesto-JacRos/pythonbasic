###
# 01 - Expresiones regulares
'''
las expresioners regulares son una secuencia de caracteres que forman un patron de busqueda.
Se utilizan para la buscqueda de cadena de texto, validacion de datos. etc
'''
'''
Por que aprender Regex ?

- Busqueda avanzada: Encontrar patrones especificos en textos grandes de forma rapida y precisa 
(in editor de markdown solo usando regex)

- Validacion de datos: Asegurate que los datos que ingresa el usario como elemail, telefono, etc. que sean correctos

- Manipulacion de texto: extraer, reemplazar y modificar partes de la cadena de texto facilmente.

- 

'''
import os
os.system('cls')
# 1. Importar el modula de expresiones regulares 'rex'
import re 
# 2. Crear un patron, que es una cadena de texto que decribe lo que queremos econtrar 
pattern = 'Hola'
# 3. texto dodne queremos buscar
text = 'Hola Mundo'
# 4. Usar la funcion de busqueda de 're'
# primer arguemnto = texto a buscar, segundo argumento = txt donde buscarlo 
# En Python, los objetos tienen un valor de verdad (truthy / falsy)
# 🧠 Regla clave
# None → ❌ False
# Objeto Match → ✅ True

result = re.search(pattern, text)
if result:
    print('He encontrado el praton de texto')
else:
    print('No he encontrado el patronde texto')

print('Metodos de Re en Python')

# group() devuelve la cadena que coincide con el pattern 
# en este caso es la cadena 'Hola'
print(result.group())

# start() devolver la posicion inicial de la coincidencia 

print(result.start()) # devuelve 0 ya que es inicia en el primer indice que es 0 

# end()  devolver la posicion final de la coincidencia 

print(result.end()) # devuelve 4 porque hasta ese indice termina, o sea que aunque sea 3 el indce 
# dodne se encuentra la 'a' devuelve el sigueinte indice

print('Ejercicos de regex')

# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. " 
"Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = 'IA'

found_ia = re.search(pattern, text)

if found_ia:
    print(f'He encontrado el patron en el texto en la posicion {found_ia.start()} y termina en la posicion {found_ia.end()} ')
else: 
    print('No he encontrado el patron en el texto')

# -------------------------------------------------------------
### Encontrar todas las coincidencias de un patron
# findall() devualve una lista con todas las coincidencias 

text = 'Me gusta Pyhhon, Python es lo maximo, aunque Python no es tan dificil, ojo con Python'
pattern = 'Py....'# el punto representa cualqueir caracter
# con eso aun que hemos cambiado la tercera letra con el punto , nos devuelve todas las considencias 
matches = re.findall(pattern, text)
print(matches)
# como es una lista lo que devuelve, puedes usar todos los metodos para listas

print('numero de coincidencias: ', len(matches))

# ___________________________________________________________

# iter() devuelve un iterador que contiene todos los resultados de la busqueda 
# es para recorrer todas las coincidencias comon objetos Match

matches = re.finditer(pattern, text) # 
print('Matches: ', matches)
for match in matches: 
    print(match.group(), match.start(), match.end())



# EJERCICIO 02
# Encuentras todas las ocurrencias de la palabra 'jacros' en el siguiente texto e indica la posicion en que enmpieza y termina cada coincidencia y cuantas veces lo encontro


text = 'Es es el curso de de Python de jacrosdev. Suscribite  a jacrosdev si te gusta este contenido! jacros'

parttern_ = 'jacros'

find_partten_ = re.findall(parttern_, text)
print('Lista de ocurrencias ', find_partten_)
print('veces encontrada: ', len(find_partten_))
find_partten_ = re.finditer(parttern_,  text)

for match  in find_partten_:
    print(match.group(), match.start(), match.end())

print()
def title(title):
    print()
    print(f'----------------{title}-------------------')
    print()

print()
title('Modificadores de en busquedas')
# Modificadores 
# los modificadores son opciones que se pueden agregar a un patron para cambiar su comportamiento
# re.IGNORECASE: Ignora las matusculas y minusculas
#  


text = ("Todo el mundo dice que la IA nos va a quitar el trabajo. " 
"Pero, la ia no es tan mala. Viva la Ia")
pattern12 = 'IA'

found_ia = re.findall(pattern12, text, re.IGNORECASE) #como 

if found_ia:
    #print(f'He encontrado el patron en el texto, en la posicion {found_ia.start()} y termnina en la posicion {found_ia.end}')
    print(found_ia)
title('Ejercicio 3')
# EJERCICIO 03 
# Encuentra todas las ocurrencias de la palabra "python" en el
# sigueinte textom sin distinguir entre mayuscula y minusculas

text = 'Es es el curso de Python de jacrosdev. Suscribete a python si te gusta este contenido! PYTHON'

patron = 'python'
patron_encontrado = re.findall(patron, text, re.IGNORECASE)
if patron_encontrado:
    print(patron_encontrado)

### Reemplzar texto
title('reemplzar con .sub()') 
# .sub() reemplzar todas las coincidencia de un patrond e texto 

text = 'Hola, mundo!, Hola de nuevo.'
pattern = 'Hola'
replacement = 'Adios'
new_text = re.sub(pattern,  replacement, text)
print(new_text)


