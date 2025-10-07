def contagem(texto):
    vogais = 'aeiou'
    quantidade = 0

    for letra in texto.lower():
        if letra in vogais:
            quantidade +=1
    return quantidade
texto = input('Digite um texto: ')

print(f'o texto contém {contagem(texto)} vogais')        


