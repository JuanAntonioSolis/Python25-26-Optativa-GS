#Tuplas son listas inmutables
asignaturas = ("servidor","base de datos","despliegue","diseño","optativa")
print(asignaturas)

# Longitud tupla
print(len(asignaturas))

print(asignaturas[2]) # despliegue

# Buscar un elemento
print(asignaturas.index("optativa")) #4

# Cortar tuplas
print(asignaturas[0:3])

# Convertir tupla en lista
asignaturas_lista = list(asignaturas)
print(asignaturas_lista)
asignaturas_lista.append("proyecto integral")
print(asignaturas_lista)

# Preguntar si elemento está en la tupla
print("montaje" in asignaturas) #false

# Unir tuplas
asignatura2do = ("sistemas", "entornos")
asignaturas += asignatura2do
print(asignaturas)
