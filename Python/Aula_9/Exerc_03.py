ano_virgente = 2023
while True:
    ano_nasc = int(input('Digite sua idade: '))
    print()
    print(f'você nasceu em {ano_virgente - ano_nasc}')
    print()
    while True:
        opc = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if opc == 'S' or opc == 'N':
            break
    if opc == 'N':
        print('Programa Finalizado!')
        print()
        break
    print()