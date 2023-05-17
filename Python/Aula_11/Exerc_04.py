def lista_unica(lista: list) -> list:
    lista_nova = []
    for num in lista:
        if num not in lista_nova:
            lista_nova.append(num)
    return lista_nova

lista = lista_unica([1, 2, 2, 3, 4, 4, 5, 3, 6, 7, 6, 8])
print(lista)