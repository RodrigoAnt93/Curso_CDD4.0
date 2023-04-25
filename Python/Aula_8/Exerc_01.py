usuario = []
senha = []
for x in range(5):
    usuario.append(input('Nome: ').strip())
    senha.append(input('Senha: ').strip())
    print()
novo_usuario = input(('Digite o usuário: ')).strip()
nova_senha = input(('Digite a senha: ')).strip()
confirmacao_usuario = False
for y in range(5):
    if novo_usuario == usuario[y]:
        if nova_senha == senha[y]:
            confirmacao_usuario = True
            break
if confirmacao_usuario:
    print('Login efetuado com sucesso')
else:
    print('Senha inválida')
