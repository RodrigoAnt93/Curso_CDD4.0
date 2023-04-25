usuario = []
senha = []
for x in range(5):
    usuario.append(input('Nome: ').strip().title())
    senha.append(input('Senha: ').strip())
    print()
for x in range(5):
    print(f'O usuário é {usuario[x]} e a senha é {senha[x]}')
