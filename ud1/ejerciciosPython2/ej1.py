'''
Crea una funcion que reciba una lista de números y retorne un diccionario
con la media, mediana y moda
'''

from statistics import *

def calcular_estadisticas(lista):
    print(mean(lista))
    print(median(lista))
    print(mode(lista))

numeros = [1,2,2,3,4,5,5,5,6]

resultado = calcular_estadisticas(numeros)