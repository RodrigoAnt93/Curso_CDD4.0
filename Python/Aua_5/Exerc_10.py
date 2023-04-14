senha = str(input('Digite a senha: '))
print(f'Senha salva: {"*"*len(senha)}')
chance = 3
acesso_acerto = True
print('')
while chance != 0 and acesso_acerto:
    try_password = str(input('Digite seu senha: '))
    if senha == try_password:
        print('Acesso liberado')
        acesso_acerto = False
    else:
        print('Senha inválida!')
        chance -= 1
    if chance == 0:
        print('Você excedeu as tentativas de senha. Sua senha foi BLOQUEADA.')
