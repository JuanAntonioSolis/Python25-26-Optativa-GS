import os
from statistics import mean
#No hace falta poner modulo delante
from math import *
from random import random, randint

print("Carpeta actual:", os.getcwd())

#print("Create folder trash:", os.mkdir('trash'))

data = [10,20,30,40,50]

#Statistics
print("La media de data es:", mean(data))

#Math
print("La raiz cuadrada de 16", sqrt(16))
print(pi)
print(pow(2,5))

#Random
print(random()) #Valor de 0 entre 0.99999
print(randint(1,10))

