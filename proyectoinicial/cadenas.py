texto = 'Hola mundo'
texto2 = "esto de programar... mal asunto"

print(texto, texto2)

texto3 = texto2 + " - " + texto

print(texto3)

#len() longitud de una cadena
print(len(texto3))

#\n salto de línea
print("me gusta 'Python' \nestoy aprendiendo mucho")

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
#%.2f establece el número de decimales a mostrar %.3f, %.1f...
print('The area of circle with a radius %d is %.2f.' %(radius, area))

#Acceso  a string por índice
cadena = "I love New York"
print(cadena[0])
print(cadena[0:4])

print(cadena[len(cadena)-1])
print(cadena[-1])

#Reverse 
print(cadena[::-1])