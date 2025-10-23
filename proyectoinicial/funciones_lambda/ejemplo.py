from math import pi 
from functools import reduce

cuadrado = lambda x: x * x

print(cuadrado(5))

area_circulo = lambda r: pi*cuadrado(r)
print(area_circulo(45.23))

#Uso de map, filter y reduce con funciones lambda

#Map -> aplicar una funcion a cada elemento de la lista
lista = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = list(map(lambda n: n * n, lista))
print(lista_cuadrados)

#Filter -> Eliminar los elementos de la lista que no cumplan la condición
lista2 = [3,4,6,15,28,25]
lista_multiplos_cinco = list(filter(lambda x: x % 5 == 0,lista2))
print(lista_multiplos_cinco)

#Reduce -> Aplicar una función de varios parámetros a un único resultado, se va aplicando a la lista
#Importar functools 
lista3 = [1,2,3,4,5]
total_multiplicado = reduce(lambda x, y: x*y,lista3)
print(total_multiplicado)

