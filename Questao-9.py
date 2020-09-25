#Crie um programa em Python que receba uma lista com 10 elementos informados pelo usuário
# (numéricos ou textuais), e salve seu conteúdo em um arquivo .txt criado em tempo de execução.
arquivo = open('texto.txt', 'a')

frases = list()
frases.append('Vamo \n')
frases.append('Beber ? \n')
frases.append('Sim \n')
frases.append('Claro \n')
frases.append('Começando \n')
frases.append('Agora. \n')
frases.append('Só \n')
frases.append('Entregue \n')
frases.append('a \n')
frases.append('Prova do Douglas \n')

arquivo.writelines(frases)