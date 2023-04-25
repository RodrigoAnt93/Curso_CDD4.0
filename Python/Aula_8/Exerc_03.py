lista_num = []
contador = 0
for x in range(10):
    lista_num.append(int(input('Digite um valor: ')))
print()
valor = int(input('Digite um valor: '))
for y in range(10):
    if valor == lista_num[y]:
        contador += 1
print()
print(f'O valor foi encontrado {contador} vezes.')