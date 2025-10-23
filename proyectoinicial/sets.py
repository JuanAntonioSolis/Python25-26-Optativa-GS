# Colección desordenada de elemenos únicos, sin duplicados
compra = set()
compra.add("Huevos")
compra.add("Mantequilla")
compra.add("Agua")

print(compra)
print(len(compra))

# Para añadir varios elementos a la vez
compra.update(["carne","leche","Agua"])
print(compra)

# Eliminar objetos --> discard better than remove
compra.remove("carne")
compra.discard("leche") # No da error si el elemento no existe
print(compra)

# De lista a set
lista = ['banana','naranja','mango','limon','naranja']
frutas = set(lista)
print(frutas)

# OPERADORES DE CONJUNTOS
A = {1,2,3,4,5}
B = {4,5,6,7,8}

# Union -> elementos que están en A o en B
print(A | B)
print(A.union(B))

# Intersección -> elementos que están en A y en B
print(A & B)
print(A.intersection(B))

# Diferencia -> elementos que están en A pero no en B
print(A - B)
print(A.difference(B))
print(B - A)
print(B.difference(A))

# 