numero = int(input('Digite o numero da tabuada: '))
print('')
print(f'A tabuada de {numero} é: ')
for num in range(1,11):
    print(f'{num} X {numero} = {num * numero}')