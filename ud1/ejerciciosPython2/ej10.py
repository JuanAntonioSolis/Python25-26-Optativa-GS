'''
Usa filter() con lambda para obtener solo los números que sean divisibles 
por 3 Y por 5 (es decir, divisibles por 15) de una lista.
'''

numeros = [15, 30, 7, 45, 60, 12, 90]

divisibles = list(filter(lambda x: x % 15 == 0, numeros))

print(divisibles)