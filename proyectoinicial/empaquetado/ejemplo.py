# *variable -> empaquetar los elementos restantes en una lista
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries

print(fin)
print(sw)
print(rest)

def multiplicar(*params):
    for i in params:
        print(i * 5)

multiplicar(1,2,3,4,5)
