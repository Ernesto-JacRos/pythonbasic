import os
os.system('cls')

numero = -1 
while numero <= 0:
    try:
        numero = int(input('Escribe un numero positivo: '))
        if numero < 0:
            print('el numero debe ser positivo, intenta d enuevo ')
    except:
        print('lo que introduces debe ser un numero, si no no funciona')
    
print(f'El numero que has introducido es: {numero}')