tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
play = 1
wins = False
jogadas = 1
while True:
    print("    0   1   2")
    print("  ┌───┬───┬───┐")
    print(f"0 | {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} |")
    print("  ├───┼───┼───┤")
    print(f"1 | {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} |")
    print("  ├───┼───┼───┤")
    print(f"2 | {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} |")
    print("  └───┴───┴───┘")
    #Conferir se existe um vencedor.
    if wins:
        if play == 1:
            print("\033[0;34mParabéns Play 2!! Você venceu o jogo!!\033[m")
            break
        else:
            print("\033[0;32mParabéns Play 1!! Você venceu o jogo!!\033[m")
            break
    else: #Se chegar em 10 jogas é por que deu empate.
        if jogadas >= 10:
            print("\033[0;31mO jogo terminou empatado!\033[m")
            break

    print("Vez do \033[0;32mPlay 1\033[m:" if play == 1 else "Vez do \033[0;34mPlay 2\033[m:" )
    while True: #Tratamento para o jogador só escolher linha e coluna de 0 à 2.
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        if linha <= 2 and coluna <= 2:
            break
        else:
            print("\033[0;33mDigite um valor de linha e coluna válido.\033[m")
    #Marcar o quadrado escolhido, antes verificar se o quadrado já foi marcado.
    if play == 1:
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = "\033[0;32mX\033[m"
            play = 2
        else:
            print("\033[0;33mEsse quadrado já foi marcado. Escolha um vazio.\033[m")
            print('=-=' * 15)
            continue
    else:
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = "\033[0;34m0\033[m"
            play = 1
        else:
            print("\033[0;33mEsse quadrado já foi marcado. Escolha um vazio.\033[m")
            continue

    #Verificar a ordem dos quadrados marcados para saber se tem vencedor.
    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] and tabuleiro[0][0] != " ":
        wins = True
    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] and tabuleiro[1][0] != " ":
        wins = True
    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] and tabuleiro[2][0] != " ":
        wins = True
    elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] and tabuleiro[0][0] != " ":
        wins = True
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] and tabuleiro[0][1] != " ":
        wins = True
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] and tabuleiro[0][2] != " ":
        wins = True
    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != " ":
        wins = True
    elif tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2] and tabuleiro[2][0] != " ":
        wins = True

    jogadas += 1
    print('=-=' * 15)
print()
print('Fim do jogo!')