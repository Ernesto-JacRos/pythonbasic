import re
import os
os.system('cls')
# []: Coincide con cualquier caracter dentro de los carchetes 
username = 'rub.$ius_69+'
pattern  = r'^[\w._%$+-]+$'# un guion entre los corchetes puede ser un rango

matches = re.search(pattern, username)
if matches:
    print('El nombnre de usario es valido: ', matches.group())
else: 
    print('El nombre de usario no es valido')

# buscar todos las vocales de una palabra 

text = 'Hola Mundo'
pattern  = r'[aeiou]'
matches = re.findall(pattern, text)
print(matches)

# Una Regex  para encontrar las palabras man, fan, ban
# pero ignora el resto

text = 'man ran fan ñan ban'
pattern = r'[mfb]an'
matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# solo queremos las palabras man fan y ban
text = 'omniman fanatico man bandana'
pattern = r'\b[mfb]an'
matches = re.findall(pattern, text)
print('Ejercicio')
print(matches)

text = '22'
patterm = r'[0-2]' # rangons de numeros 
matches = re.findall(patterm, text)
print(matches)

# rangos de minuscula sy mayusculas 

r'[a-z]'# rango de minusculas 
r'[A-Za-z0-9áéíóúñ]+'

# [^]: Coincide con cualquier caracter que no este dentro de los corchetes 
text  = 'Hola mundo'
pattern = r'[^aeiou]' # NEGACION, devuelve todo lo que no este delntro de los corchetes en este caso todas consonantes 
# incluso los espacios 
matches = re.findall(pattern, text)
print(matches)

 