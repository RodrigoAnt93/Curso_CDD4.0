a = [10, 5, 7, 8, 6, 9, 8, 2, 6, 1]

x = int(input('Digite um número para ser o multiplicador: '))
m = list()
for num in a:
    m.append(num * x)
print()
for num in m:
    print(num)

