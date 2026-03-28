###
# 05 - Entrada de usario (input()) - version simplificada
# La funcion input() permite obtener datos de usario a traves de la consola 
###
print('Hola, Cual es tu nombre?')
name: str = input()
print(f'Your name is: {name}')  
name = input("Hi whats your name; \n") #input puede recibir un str para hacer a pregunta 
print(f'Your name is: {name}')
age: int = int(input('Whats is your age? \n'))
print(f'your age is: {age}')
#Obter varios valores con un solo input con la funcion split() y que va a reconocer valores por espacioss
country,  city = input('En que pais y ciudad vives?\n').split()#split() regres un list de str
print(f'Vives en: {country}, {city}')