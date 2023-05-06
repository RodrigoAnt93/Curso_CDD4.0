ano = int(input('Você tem quantos anos? '))
mes = int(input('E meses? '))
dia = int(input('E dias? '))

dias_total = (ano * 365) + (mes * 30) + dia
print()
print(f'Você tem {dias_total} dias de vida vivido.')