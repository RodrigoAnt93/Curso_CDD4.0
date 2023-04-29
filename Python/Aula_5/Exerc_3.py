negativo = 0
for num in range(10):
    perg = int(input('Digite um valor: '))
    if perg < 0:
        negativo += 1
print(f'Nesses valores passados {negativo} foram negativos.')