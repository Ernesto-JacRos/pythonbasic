###
# 02 - Booleans 
# Valores logicos: True (Verdadero) y False (Falso)
#Fundamentales en el control de flujo y logica en progrmacion
###

print('Vaores Booleanos basicos')
print(True)
print(False)
#Operadores de comparacion 
print('Operadores de comparacion')
print('5 > 3', 5 > 3 ) # True
print('5 < 3', 5 < 3 ) # False
print('5 == 35', 5 == 3 ) # True (de igualda)
print('5 != 3', 5 != 3 ) # True (de desigualda )
print('5 >= 5', 5 >=5 ) # True (mayor o igual que )
print('5 <= 3', 5 <= 3 ) # False (menor o igaul que)

print('comparacion de cadena de texto')
#las comparaciones de cadenas d etexto en python son lexicograficas 
print('manzana < pera: ', "manzana" < "pera" )# hace la comparacion alfabeticamnete
#y si la primer letra es igual hace la comparacion con a segunda, sucesivante 
# es sensible a minuscula sy mayuscuas 
print("'Hola' == 'hola'", "Hola" == "hola" )

numero = 5 # es distinto a 0 por ende es true
if numero: 
    print('el numero no es cero')

numero = 0 #sabemos que es False 
if numero:
    print('aqui nunca entra')
nombre = " "
if nombre:
    print('el nombre no es vacio')

print('\noperadores Ternarios')
print('la condicion ternaria ')
# es la forma concisa de un if-else en una linea de codigo
# [codigo  si cumple la condicion] if [condicion] else [codigo si no cumple]

edad = 17 
mensaje = 'Es mayokr de edad' if edad >= 18 else 'Es menor de edad'
print(mensaje)
print( 'Es mayokr de edad' if edad >= 18 else 'Es menor de edad')
#python muy verbosidad



