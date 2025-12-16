num1 = int(input("Escribe un número:"))
num2 = int(input("Escribe otro número:"))

if num1 > num2:
    num1,num2 = num2,num1 #Intercambio de variables

for i in range(num1,num2+1):
    if i % 2 == 0:
        print(i)

