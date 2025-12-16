'''
Genera una lista con los cuadrados de los 
números pares del 1 al 50 usando list comprehension.
'''
from math import *

cuadPares = [num for num in range(1,51) if num %2==0]

for num in cuadPares:
    print(pow(num,2))