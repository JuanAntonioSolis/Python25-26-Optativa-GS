cadena = "Hola mundo"

lista = [letra for letra in cadena if letra in 'aeiou']

print(lista)

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers)  

#Numeros pares del 0 al 40
pares = [num for num in range(41) if num %2==0]

print(pares)


