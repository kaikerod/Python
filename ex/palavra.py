palavras_longas = []

paragrafo = str(input('Digite seu parágrafo: '))

for palavra in paragrafo.split():
    if len(palavra) >= 10:
        palavras_longas.append(palavra)

if len(palavras_longas) > 0:
    print(f'As palavras longas são: {palavras_longas}')
else:
    print('Não há palavras longas no parágrafo.')