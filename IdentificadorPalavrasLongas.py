def identificador(texto):
    quantidade = 0

    for palavras in texto.split():
        if len(palavras) > 10:
            quantidade +=1  
    return quantidade        
        
frase = input("Digite uma frase: ")

print(f'Palavras longas encontradas {identificador(frase)} ')







