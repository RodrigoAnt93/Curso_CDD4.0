total_votos = int(input('Total votos da cidade: '))
branco = int(input('Votos brancos: '))
validos = int(input('Votos válidos: '))
nulos =  int(input('Votos nulos: '))
porc_branco = (branco / total_votos) * 100
porc_validos = (validos / total_votos) * 100
porc_nulos = (nulos / total_votos) * 100
print()
print(f'Votos válidos foram {porc_validos}%, votos brancos foram {porc_branco}% e votos nulos foram {porc_nulos}%'
      if (branco + nulos + validos) <= total_votos else 'Quantidade de votos errados')