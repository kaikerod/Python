frase = input('Digite uma frase e direi quantas vogais ela possui: ')
vogais = []

# Minha versão força bruta:

for vogal in frase:
    if vogal == 'a' or vogal =='e':
        vogais.append(vogal)
    elif vogal == 'i' or vogal == 'o':
        vogais.append(vogal)
    elif vogal == 'u':
        vogais.append(vogal)

print(f'Esta palavra tem {vogais}.')

# -------------------------------------------------------

# Versão mais eficiente:

frase = input('Digite uma frase: ').lower()
vogais = []

for letra in frase:
    # Tradução: "Se a letra estiver dentro do texto 'aeiou'..."
    if letra in 'aeiouáéíóúãõ': # Você pode até adicionar acentos aqui facilmente!
        vogais.append(letra)

print(f'Encontrei as vogais: {vogais}')
print(f'Total de vogais: {len(vogais)}')