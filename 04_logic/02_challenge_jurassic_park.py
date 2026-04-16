"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, 
depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que
 cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) 
aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y 
devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros
 (es decir, la suma de todos los números pares en la lista).
""" 

def count_carnivore_eggs(egg_counts: list) -> int:
    '''
    Esta funcion una lista de numeros enteros que representan la cantidad de huevos que han puesto 
    los diferentes dinosaurios en el parqure jurasico y lso numeros par sonde carnivoros.
    Devuelve un numero con la suma de todos los huevos de carnivoros
    '''
    egg_t_rex = []
    for egg in egg_counts:
        if egg % 2 == 0:
            egg_t_rex.append(egg)
    return sum(egg_t_rex)

print(count_carnivore_eggs([1, 2, 3, 4, 5, 6]))
