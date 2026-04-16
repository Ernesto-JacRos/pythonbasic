"""
Dado un array de números y un número goal, encuentra los dos primeros números del
 array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""
import os
os.system('cls')
nums = [1, 3, 3, 2]
goal = 8

def find_sum(lista, meta):
    for ls in range(len(lista)):
        for ls2 in range(ls + 1, len(lista)):
            if lista[ls] + lista[ls2] == meta:
                return [ls, ls2]
    return None
            
print(find_sum(nums, goal))