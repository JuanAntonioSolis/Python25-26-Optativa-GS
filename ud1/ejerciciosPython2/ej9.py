'''
Usa una función lambda con sorted() para ordenar una lista de tuplas 
(nombre, edad, altura) por edad de menor a mayor.
'''

personas = [("Ana", 25, 165), ("Juan", 30, 175), ("María", 22, 160)]

personasOrdenadas = sorted(personas,key=lambda age: age[1])

print(personasOrdenadas)