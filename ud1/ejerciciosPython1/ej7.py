numerin = int(input("Escribe un número para calcular su factorial"))
factorial = 1

for i in range (1,numerin+1):
    factorial *= i
    

print("El factorial de", numerin, "es igual a", factorial)