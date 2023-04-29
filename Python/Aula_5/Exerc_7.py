soma = 0
cont = 0

while cont < 10:
    perg = float(input('Digite um valor: '))
    soma += perg
    cont += 1
media = soma / 10

print(f'A média aritmética é {media:.2f}')

