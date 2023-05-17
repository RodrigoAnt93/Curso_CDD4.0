def calculare_estoque(produto: str, quantidade: int, valor: float) -> tuple:
    return produto, quantidade*valor


estoque = calculare_estoque('maça', 5, 5)
print(f'O estoque de {estoque[0]} é um total de R${estoque[1]}')