###
# 01 - Sentencias condicionales (if, elif else)
# Permiten ejecutar bloques de codigo solo si cumplen ciertas condiciones.
###
import os 
os.system("cls")

print('\nSentencia simple condiciona')
age = 18 
if  age >= 18:
    print('eres mayor de edad')
    print('Felicidades!')

ege = 15
if age >= 18:
    print('Eres mayor de edad ')
    print('Felicidades')

print('\n Sentencia condicional con else')
age = 15
if age >= 18:
    print(f'Eres mayor de edad')
else:
    print('Eres menor de edad') 

print('\n Sentencia condicional elif')
nota =7 
if nota >= 9:
    print('sobre saliente')
elif nota >= 7:
    print('notable')
elif nota >= 5:
    print('Aprobado')
else:#no es obligario 
    print('No esta calificado')

print('\nCondiciones multiples')

edad = 16
tiene_canet = False

print('Operadores logicos')

if edad >= 18 and tiene_canet:# con "and" todas los condicones deben ser verdaderas 
    #pudes encadenar tantas como quieras 
    print('Puedes conducir')
else: 
    print('Policia')

#Isla Margarita 
print('Sentencia Or ')
if edad >= 18 or tiene_canet:
    print('Puedes conducir en Isal ')
else: 
    print('Paga a la policia y te deja conduccir ')
print('usando not como negacion ')
es_fin_semana = False
if not es_fin_semana: # se usa not como el ! en ja 
    print('Jacros, Haya que stremear')

print('IF anidados')
#no muy recomendable
edad = 34
have_money = False
if edad >= 18:
    if have_money:
        print('Puedes ir a la discoteca')
    else:
        print('Queda te en casa')
else:
    print('No puedes entrar a la discoteca')










    