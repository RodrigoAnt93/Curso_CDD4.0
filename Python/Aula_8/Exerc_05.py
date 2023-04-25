lista_num = []
for x in range(10):
    lista_num.append(int(input('Digite um valor: ')))
print('=-=' * 20)
for z in range(10):
    if lista_num[z] % 2 == 0:
        print(f'{lista_num[z]}, ', end='')
print('=-=' * 20)
acumulador = 0
maior_valor = 0
menor_valor = 0
maior_media = 0
for y in range(10):
    acumulador += lista_num[y]
    if y == 0:
        menor_valor = lista_num[0]
        maior_valor = lista_num[0]
        continue
    if lista_num[y] > maior_valor:
        maior_valor = lista_num[y]
    if lista_num[y] < menor_valor:
        menor_valor = lista_num[y]
print(f'O menor valor é {menor_valor} e o maior é {maior_valor}')
print('=-=' * 20)
media = acumulador / 10
for c in range(10):
    if lista_num[c] >= media:
        maior_media += 1
print(f'{maior_media} números foram maior que a média.')