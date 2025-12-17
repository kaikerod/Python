dicionario = {}
palavras_repetidas = []

frase = input('Digite uma frase: ')
dicionario['frase'] = frase

for palavras in dicionario['frase']:
    
    if palavras in palavras_repetidas:
        print(f'A palavra {palavras} repetiu {palavras_repetidas.count(palavras)} vezes')
    else:
        palavras_repetidas.append(palavras)

# Lorem ipsum dolor sit amet consectetur adipisicing elit. Reprehenderit cum nesciunt fugit, nemo tempora consequuntur rerum voluptas voluptatibus voluptate in sunt adipisci et! Ratione sit, architecto necessitatibus tempore incidunt maxime.