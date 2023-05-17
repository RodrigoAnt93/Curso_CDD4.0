def texto(texto: str) -> tuple:
    texto_reverse = ''
    texto = ''.join(texto.split())
    quantidade = len(texto)
    for letra in texto[::-1]:
        texto_reverse += letra
    return quantidade, texto_reverse


texto_ = texto('Boston in 7')
print(f'O texto tem {texto_[0]} letras e a frase ao contrário fica: "{texto_[1]}"')