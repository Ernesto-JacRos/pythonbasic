### 
# 02 - Metacaracteres so simbolos espaciales con significados 
# espaciales en las expresiones regulares 
### 
import re
import os
os.system('cls')

def title(cadena):
    print()
    print(f'--------------------------{cadena}-------------------------')
    print()
# 1. el punto (.)
# Coincidir con cualquier caracter excepto una nueva linea.

title('Metacaraxter punto')
text = 'Hola mundo. H0la de nuevo, H$la otra vez'
payttern = 'H.la' # Hola, H0la, H$la

found = re.findall(payttern, text)
print(found)

title('r para representar que es una expresion regulas')

title('Metacaraxter punto')
text = 'Hola mundo. H0la de nuevo, H$la otra vez'
payttern = r'H.la' # represenatdoq que estamos haciendo uan expresion regulkar 

found = re.findall(payttern, text)
print(found)


title('Bucar pubntos pero que no sea un comidin')

# Como usar la barra invertida para anular el significado especial de un simbolo
text = 'Mi casa es blanca. y el cohce es negro.'
pattern =r'\.'
found = re.findall(pattern, text )
print(found)

title('buscar digitos en python')

# \d coincide con cualquier digito(0-9)

text = 'el numero de telefono es; 123456789'
found = re.findall(r'\d', text)
#  digito(general o espexifico) que se repite 9
found_1 = re.findall(r'\d{9}', text) 
print(found)
print('con numero de repeticiones: ',  found_1)

# Ejercicio: Detectar si hay un numerode Espanha en el texto gracias al prefijo +34

text = 'Mi numero de telefono es: +34 688999999 apuntalo vale?'
pattern = r'\+34 \d{9}'
found = re.search(pattern, text)
if found:
    print(f'Encontre el numero de telefono: {found.group()}')



# Coincide con caracteres alfanumericos 
# \w Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)

#ignora @'s % todo que sno sea alfanumerico
text = '@@@el_jacros_69&&'
pattern = r'\w'
found = re.findall(pattern,  text)
print(found)

#Espacios en blanco en python

# \s: Coincide con cualquier espacio en blanco (espacio, tabulacion, salto de linea)

print('\s para espacios tabulaciones saltos de linea')
text = 'Hola mundo\n Como estas?\t'
pattern = r'\s'
matches = re.findall(pattern, text)
print(matches)

# Validacion de cadenas de texto en python 
print('coincide con el principio de una cadena')
print('el simbolo \'^\' es para sea el inicio de la cadena, o sea que no sa #,@ etc, \n que sea alfanumerico ')
user_name = '432_name'

pattern = r'^\w'
valid = re.search(pattern, user_name)

if valid: print('El nombre del usuario es valido')
else: print('El nombre de usario no es valido')

#  ^ PARA EL INICIO, \+ EL CARACTER QUE SIGUE \D PARA QUE SIGA UN DIGITO {1,3} EL RANGO DE DIGITOS
#  Y UN ESPACIO PARA QUE BUSXQUE EL ESPACIO DESPUES DEL RANGO 

phone = '+34 688999999'
pattern = r'^\+\d{1,3} '
valid = re.search(pattern, phone)
if valid: print('El numero de telefono es valido ', valid.group())
else: print('El numero de telefono no es valido')

# $: COINCIDE CON EL FINAL DE UNA  CADENA 
print('usamos $ para verificar el final de una cadena')
text = 'Hola mundo'
pattern = r'mundo$'
valid = re.search(pattern,  text)

if valid: print('La cadena es valida')
else: print('La cadena no es valida')
# Ejercicio 
# Valida que el correo sea de gmail

text = 'jacros@gmail.com'
pattern = r'^\w+@gmail.com$'
valid = re.findall(pattern, text)

if valid: print('El correo gmail es valido')
else: print('el correo no es valido')

# Ejercicio 
# Tenemos una lista de archivos, necesitamos saber los nombres 
# de los ficheros con extension txt
# 
text = 'file1.txt file2.pdf jacros-of.webp secret.txt'

pattern = r'[\w]+\.txt'
valid = re.findall(pattern, text)
print(valid)

# Palabra exacta en python 
# \b: Coincide con el principio o final del la palabra 

print(' \ b si coincide con principio o final de una palabra ')
# se tiene poner con \b porque si hay espacio no lo va encontrar
text = 'casa, casada, casado, cascada, casa'
pattern = r'\bcasa\b'
found = re.findall(pattern, text)
print(found)

# Coincidencias con opciones
# | [or]: Coincidir con una opcion u otra
fruits = 'planatano, manzana, aguacate, pera, palta, aguacate, pera, palta, aguacate, pera, palta'
pattern = 'palta|aguacate|p..a|\w{6}|\b\w{7}\b'# pueden ser varios or |
matches =  re.findall(pattern, fruits)
print(matches)

# Cuantificadores 
print('Cuantificadores')









