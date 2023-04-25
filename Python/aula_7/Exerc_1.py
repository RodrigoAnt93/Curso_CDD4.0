quant_aluno = int(input('Quantos alunos? '))
alunos = []
for c in range(quant_aluno):
    alunos.append(input(f'Digite o nome do {c+1}° aluno: ').strip().title())
print()
cont = 0
for aluno in alunos:
    print(f'{cont} é a posição de {aluno}')
    cont += 1