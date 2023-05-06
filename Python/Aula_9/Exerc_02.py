while True:
    while True:
        num = int(input('Digite um número: '))
        if num != 0:
            break
        else:
            print('Digite um valor diferente de zero.')
            print()
    if num > 0:
        print('O valor é positivo.')
    else:
        print('O valor é negativo.')
    while True:
        opc = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if opc == 'S' or opc == 'N':
            break
    if opc == 'N':
        print('Programa Finalizado!')
        print()
        break
    print()