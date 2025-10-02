edad = int(input("Escribe tu edad:"))

if edad < 18:
    print("Eres menor de edad")
elif edad > 18 and edad < 65:
    print("Eres adulto")
else:
    print("Eres mayor")