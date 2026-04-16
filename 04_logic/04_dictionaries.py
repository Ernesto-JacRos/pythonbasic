###
#  04 - Dictonaries
# los diccionarios son colecciones de pares clave-valor.
# Sirven para alamecenar datos relacionados entre si y
#  se pueden acceder a ellos de manera eficiente utilizando sus claves.
### 

# Ejemplo tipico de un diccionario

import os 
os.system('cls')
persona= {
    'nombre': 'Jacros',
    'edad': 30,
    'es_estudiante': True,
    'calificaciones': [8, 9, 10],
    'socials':{
        'twitter': '@jacros',
        'linkedin': 'linkedin.com/in/jacros'    
    }

}

# Para acceder a los valores
print( persona['nombre'])
print(persona['calificaciones'][2])# accediendo al tercer elemento de la lista de calificaciones
print(persona['socials']['twitter']) # accediendo al twitter dentro del diccionario socials

# cambiar valores al acceder 

persona['nombre'] = 'Ernesto'
persona['calificaciones'][2] = 12

print(persona['calificaciones']) 
print(persona['nombre'])
print(persona)

# Borrar un valor del diccionario usamos del
del persona['edad']
print(persona)


# Recuperar y eliminar un valor al mismo tiempo con pop
es_estudiante = persona.pop('es_estudiante') # elimna la propiedad y devualve su valor 
print(f'es_estudiante: {es_estudiante}')
print(persona)


# Sobreescribir un diccionario con otro diccionario con update
# lo que hace es que si hay propiedades diferentes las agrega al primer diccionario 
# y si hay propiedades iguales las sobre escribe co las valores dle segundo diccioanrio 

print()
print('Update en dicionarios ')
a = {'name': 'jacros', 'age': 30}
b = {'es_estudiante': True, 'city': 'Madrid', 'name': 'ErnestoJacrosDev'}
a.update(b) # actualiza el diccionario a con los valores de b, si hay claves iguales se sobreescriben
print(a)
# Comprobar si una propiedad existe en un diccioanrio con 'in'

print()
print('Saber si una propiedad existe')
print('nombre' in persona)# pasas la propiedad 
print('name' in  persona)

# para aobtener las keys
print('\nKeys: ')
print(persona.keys())

# Para obtener los values
print('\nvalues: ')
print(persona.values())

# para obtenes los items 
print('\nitems: ')
print(persona.items())
print('for en dicionarios')
for key, value in persona.items():
    print(f'{key} : {value}')

###
# Ejercicio de diccionario que reemplaza los for anidados 

def find_firts_sun(nums, goal):
    seen =  {} #Diccinario  para guardar el numero y si indice 

    for idx, vl in enumerate(nums):
        missing = goal - vl
        if missing in seen:
            return [seen[missing], idx]
        seen[vl] = idx # Guarda el numero actual a los vistos 
        #print(f'Iteracion {idx} - valor: {vl}')

    return None


nums = [4, 5, 6, 2  ]
goal = 8
print(find_firts_sun(nums, goal))
