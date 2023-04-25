cont = 1
acumulador = 0
alunos_notas = list()
for nota in range(5):
    alunos_notas.append(int(input(f'{cont}° Nota: ')))
for nota in alunos_notas:
    acumulador += nota
    cont += 1
print()
media = acumulador / 5
cont = 1
for nota in alunos_notas:
    print(f'A {cont}° nota foi acima da média' if nota >= media else f'A {cont}° nota foi abaixo da média')
    cont += 1