'''
Pide al usuario que introduzca una frase y construye una lista con las 
palabras que aparecen sin repeticiones, manteniendo el orden en el que aparecen.
'''

frase = input("Escribe una frase: ")

palabras = frase.split()

lista_srep = set(palabras)

print(palabras)

print(lista_srep)





