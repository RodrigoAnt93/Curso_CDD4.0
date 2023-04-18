while True:
    valor_1 = float(input('Digite um valor: '))
    valor_2 = float(input('Digite outro valor: '))
    print('')
    print('1 - Soma \n'
          '2 - Subtração \n'
          '3 - Multiplicação \n'
          '4 - Divisão\n'
          '5 - Para digitar novo número\n'
          '6 - Para sair')
    opc = int(input('Digite uma opção: '))
    if opc == 1:
        print(f'O valor de {valor_1} + {valor_2} é igual a {valor_1 + valor_2}')
    elif opc == 2:
        print(f'O valor de {valor_1} - {valor_2} é igual a {valor_1 - valor_2}')
    elif opc == 3:
        print(f'O valor de {valor_1} * {valor_2} é igual a {valor_1 * valor_2}')
    elif opc == 4:
        print(f'O valor de {valor_1} / {valor_2} é igual a {valor_1 / valor_2}')
    elif opc == 5:
        print()
        continue
    elif opc == 6:
        break
    print('=-=' * 20)
print('FIM DO PROGRAMA!')