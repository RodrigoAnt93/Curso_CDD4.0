soma = 0
for n in range(10):
    num = int(input('Digite o valor: '))
    if num % 2 != 0:
        soma += num


print(f'A soma dos números impares são {soma}')