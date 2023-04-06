alunos = int(input('Quantos alunos? '))
print('')
soma = 0
for aluno in range(1, alunos+1):
    nota = float(input(f'Nota {aluno}° aluno: '))
    soma += nota

print(f'A média dessas notas é {soma / alunos}')