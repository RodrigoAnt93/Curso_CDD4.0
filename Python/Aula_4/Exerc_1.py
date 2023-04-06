mes = int(input('Digite o número do mês que você nasceu: '))

if mes >= 1 and  mes <= 12:
    if mes == 1:
        print(f'Você nasceu no mês de Janeiro')
    elif mes == 2:
        print(f'Você nasceu no mês de Fevereiro')
    elif mes == 3:
        print(f'Você nasceu no mês de Março')
    elif mes == 4:
        print(f'Você nasceu no mês de Abril')
    elif mes == 5:
        print(f'Você nasceu no mês de Maio')
    elif mes == 6:
        print(f'Você nasceu no mês de Junho')
    elif mes == 7:
        print(f'Você nasceu no mês de Julho')
    elif mes == 8:
        print(f'Você nasceu no mês de Agosto')
    elif mes == 9:
        print(f'Você nasceu no mês de Setembro')
    elif mes == 10:
        print(f'Você nasceu no mês de Outubro')
    elif mes == 11:
        print(f'Você nasceu no mês de Novembro')
    elif mes == 12:
        print(f'Você nasceu no mês de Dezembro')
else:
    print('Você não digitou um numero válido')
