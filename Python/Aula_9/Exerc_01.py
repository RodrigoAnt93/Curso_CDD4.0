notas_alunos = []

while True:
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    notas_alunos.append(media)
    print()
    print(f'A média é {media}')
    if media >= 7 and media <=10:
        print('O aluno está aprovado.')
    elif media >= 4:
        print('O aluno está em recuperação')
    else:
        print('O aluno está reprovado')
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
print(notas_alunos)