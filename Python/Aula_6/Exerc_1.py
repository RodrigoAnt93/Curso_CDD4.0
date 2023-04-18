while True:
    while True:
        nota_a = float(input('Digite a primeira nota: '))
        if nota_a >= 0 and nota_a <=10:
            break
        else:
            print(f'Digite uma nota de 0 à 10')
    while True:
        nota_b = float(input('Digite a segunda nota: '))
        if nota_b >= 0 and nota_b <= 10:
            break
        else:
            print(f'Digite uma nota de 0 à 10')
    print(f'=-=' * 15)
    print(f'A média do aluno é {(nota_b + nota_a) / 2}')
    print('')
    while True:
        opc = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if opc == 'S' or opc == 'N':
            break
        else:
            print('Digite S ou N!')
    if opc == 'S':
        break
    print('')