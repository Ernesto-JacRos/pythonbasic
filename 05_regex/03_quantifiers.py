###
# 03 - quantifiers 
# Los cuantificadores se utilizan para especificar cuantas ocurencias
# de un caracter o grupo de caracteres se deben encontrar en una cadena
###

def title(title):
    print()
    print(f'-------------------{title}--------------------')

import re
import os 
os.system('cls')

# *: Puede aparecer 0 o mas veces 
text = 'aaaba'
pattern = 'a*' # 0 o  mas veces
matches = re.findall(pattern, text)
print(matches)
# por que la lista aparecen ''? , porque es el cero veces usando el cuantificador * 

# +: Una o mas veces

text = 'dddd aaa a ccc aa bb casa'
pattern = 'a+'
matches = re.findall(pattern, text)
print(matches)
# casa tiene dos 'a' entonces las 2 'a' las separa en la lista 
title('simbolo: ? para cero o una vez ')

text = 'aaabacb'
pattern = 'a?b' # cuantas veces aparece la b  con un 'a' puede regresar la b sin la a 
#porque como el titulo lo dice es 0 o una vez
matches = re.findall(pattern, text)
print(matches)# salida ['ab', 'b']
# en caso de que exista a antes de una b quiero que me la devuelvas 

# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto 
phone = '+34 688999999'
pattern = r'\+?34 \d{9}'

# {n}: Exactamente n veces 

#text = 'aaaaaa'# en esta cadena nos lanzara dos vesc 3a en la lista ya que encuentra 2 veces 3 veces a 
text = 'aaaaaa aa a aaaa'
pattern = r'a{3}'
matches = re.findall(pattern, text)
print(matches)

# {n , m}: De n a m veces 
#text = 'midu midumidu midumidumidu'
text = 'u uu uuu uuu u'
#pattern = r'[midu]{2,4}'
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
print(matches)

print('Ejercicio')
print()
# Ejercicio:
# Encuentra las palabras de mas de 4 letras
words = 'ala casa arbol leon cinco murcielago'
#pattern = r'\b\w{4,6}\b' delimita qeu sean palabras exactas 
pattern = r'\w{4,6}' # trunca las palabras con mas de 6 letras por eso hay poner 
matches = re.findall(pattern, words)
print(matches)

# Ejercico;
# Encuentra las palabras de mas de 6 letras
words = 'ala fantastico casa arbol leon cinco murcielago'
pattern = r'\b\w{6,}\b'
matches = re.findall(pattern, words)
print(matches)
# Sets y corchetes en Regex

