branco = int(input('Votos brancos: '))
validos = int(input('Votos válidos: '))
nulos =  int(input('Votos nulos: '))
total_votos = branco + validos + nulos
porc_branco = (branco / total_votos) * 100
porc_validos = (validos / total_votos) * 100
porc_nulos = (nulos / total_votos) * 100
print()
print(f'Votos válidos foram {porc_validos}%, votos brancos foram {porc_branco}% e votos nulos foram {porc_nulos}%')