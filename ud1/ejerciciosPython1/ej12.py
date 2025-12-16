
def es_primo(n):
    if n <= 2:
        return True
    else:
        for i in range(4,n):
            if n % i == 0:
                return False
        return True

num = int(input("Escribe un número:"))

print(es_primo(num))

