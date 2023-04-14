entre_10_20 = 0
fora_10_20 = 0
for num in range(10):
    perg = int(input('Digite um valor: '))
    if 10 <= perg <= 20:
        entre_10_20 += 1
    else:
        fora_10_20 += 1
print(f'Nesses valores passados {entre_10_20} foram entre 10 e 20. {fora_10_20} não foram.')