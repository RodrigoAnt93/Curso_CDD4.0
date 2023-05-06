quant_compra = int(input('Quantidade: '))
print(f'O valor da compra ficou R${float(quant_compra)}' if quant_compra >= 12 else f'O valor da compra ficou R${float(quant_compra * 1.3)}')