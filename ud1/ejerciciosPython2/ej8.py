'''
Dada una lista de strings, crea un 
diccionario usando comprehension donde las 
claves sean las palabras y los valores su longitud.
'''

palabras = ["Python", "Java", "JavaScript", "C++"]

dicc = [(palabra, len(palabra)) for palabra in palabras]

print(dicc)