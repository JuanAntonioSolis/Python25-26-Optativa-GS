# WHILE
i = 1
while i <= 5:
    print(i)
    i += 1

# WHILE con ELSE
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Termina el bucle")
    print(i)

print("-----------")
# break para romper bucle
i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1

print("-----------")
# continue 
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)


print("-----------")
# FOR sobre una secuencia(lista, tupla, set...)
frutas = ["apple","banana","cherry"]
for fruta in frutas:
    print(fruta)

precios = {25.95,15.50,9.99}
for precio in precios:
    print(precio)

#FOR con rango
for i in range(1,14):
    print(i)

#for del 100 al 0 solo decenas
for i in range(100,0,-10):
    print(i)

print("-----------")

# for sobre set
conjunto = {1,2,3,4,5}
for num in conjunto:
    print(num)

print("-----------")

# for sobre diccionario
persona = {"nombre": "Juan","edad":23,"sexo":"masculino"}
for clave in persona:
    print(clave, ":", persona[clave])

for clave, valor in persona.items():
    print(clave,valor)