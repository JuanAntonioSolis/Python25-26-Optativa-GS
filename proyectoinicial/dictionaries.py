# Diccionarios : son colecciones de datos que almacenan pares clave-valor:
# Las claves deben ser únicas e inmutables
# Los valores pueden ser de cualquier tipo de dato y pueden repetirse

dicc = {}
print(dicc)

persona = {"nombre": "Juan", "edad":23, "ciudad": "Almeria", "idioma":"español"}
print(persona)

# Acceder a valores por clave
print(persona["nombre"])

# Modificar valores
persona["edad"] = 22
persona["idioma"] = "ingles"
print(persona)

# Longitud
print(len(persona))

# Añadir nuevos pares clave-valor
persona["profesion"] = "Estudiante"
print(persona)

# Eliminar pares clave-valor
del persona["ciudad"]
print(persona)

# Eliminar elemento y devueelve valor
edad = persona.pop("edad")
print(edad)
print(persona)

# Eliminar el último insertado
last = persona.popitem()
print(last)
print(persona)

