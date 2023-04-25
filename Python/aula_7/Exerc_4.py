lista = []
for x in range(5):
    lista.append(int(input('Digite um numero: ')))
for x in range(-1, -6, -1):
    print(lista[x])
print()
for x in reversed(lista):
    print(x)
