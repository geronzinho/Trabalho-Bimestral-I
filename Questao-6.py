#Escreva um programa em Python que receba uma String,
# e remova os caracteres nos índices pares da palavra imputada.
# O programa deverá retornar a nova String ao usuário.
word = 'GladstonedaGlandeGrande'

index = 0
new_word = ''

while index < len(word):
    if index % 2:
        new_word += word[index]
    index = index + 1
print(f'Retornou:  {new_word}')