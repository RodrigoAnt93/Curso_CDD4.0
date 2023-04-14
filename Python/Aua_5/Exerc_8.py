quant_alunos = int(input('Quantos alunos tem na sala? '))
c = 0
soma = 0
print('=-=' * 20)
while quant_alunos != 0:
    nota_aluno = float(input(f'Digite a nota do {c+1}° aluno: '))
    soma += nota_aluno
    quant_alunos -= 1
    c += 1
print('=-=' * 20)
print(f'Foram {c} notas somadas e a média é {soma / c:.2f} ')