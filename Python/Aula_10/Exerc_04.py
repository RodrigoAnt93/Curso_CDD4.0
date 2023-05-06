inicio = int(input('Inicio: '))
final = int(input('Final: '))

if inicio < final:
    print(f'O jogo teve {final - inicio}h')
else:
    print(f'O jogo teve {(24 - inicio) + final}h')