num_1 = int(input('Digite o primeiro valor: '))
while True:
    num_2 = int(input('Digite o segundo valor: '))
    if num_1 == num_2:
        print('Valor igual ao primeiro. pfv digitar um valor diferente!')
    else:
        break
print(f'{num_1} -> {num_2}' if num_1 < num_2 else '{num_1} -> {num_2}')
