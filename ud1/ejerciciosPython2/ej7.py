'''
Dada una lista de palabras, crea una nueva lista solo con las 
palabras que tengan más de 5 letras usando list comprehension.
'''

palabras = ["sol", "python", "casa", "programación", "gato", "computadora"]

lista = [palabra for palabra in palabras if len(palabra) > 5]

print(lista)