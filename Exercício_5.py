def prepareList(attempts_words, word):
    list = []
    while(word <= attempts_words):
        print(f'Palavra {word} de {attempts_words}')
        string = (input('Adicione uma palavra à sua lista: \n'))
        list.append(string)
        word += 1
    return list

attempts_words = int(input('Deseja informar quantas palavras? : '))
word = 1
list = prepareList(attempts_words, word)

# função max possui um parâmetro chamado key em que você pode passar um objeto chamável e,
# quando definido, o retorno deste objeto para cada item da lista que será utilizado como base de comparação.
# Sendo assim, passamos o tamanho (len) para ser comparado
foundMaxWord = max(list, key=len)


print(f'Maior palavra da lista: {foundMaxWord} com {len(foundMaxWord)} caracteres')
