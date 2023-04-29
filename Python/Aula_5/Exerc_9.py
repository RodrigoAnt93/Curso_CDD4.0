num_1 = float(input('Digite o primeiro valor: '))
confere = True
while confere:
    num_2 = float(input('Digite o segundo valor: '))
    if num_2 == 0:
        print('Não se divide nada por zero!')
        print('')
    else:
        confere = False
print('=-=' * 15)
print(f'O resultado da divisão é {num_1 / num_2:.2f}')

