numeros = []
for x in range(3):
    numeros.append(int(input('Digite um valor: ')))
maior = numeros[0]
menor = numeros[0]
for y in range(3):
    if numeros[y] > maior:
        maior = numeros[y]
    if numeros[y] < menor:
        menor = numeros[y]
print()
print(f'O maior valor é {maior} e o menor é {menor}')