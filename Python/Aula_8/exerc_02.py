a = []
b = []
c = []
opc = int(input('Quantos valores tem no vetor? '))
for x in range(opc):
    a.append(int(input('Digite o valor do vetor A: ')))
    b.append(int(input('Digite o valor do vetor B: ')))
    c.append(a[x] + b[x])
    print()
print(c)
