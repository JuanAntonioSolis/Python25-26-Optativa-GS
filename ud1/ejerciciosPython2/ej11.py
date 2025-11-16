'''
Convierte una lista de temperaturas en Celsius a 
Fahrenheit usando map() y lambda. La fórmula es: F = (C × 9/5) + 32

'''

celsius = [0, 10, 20, 30, 40]

fahrenheit = list(map(lambda x: (x*9/5) + 32,celsius))

print(fahrenheit)