# Faz a leitura da string e converte em um array separando por virgula
numbers = input('Insira 3 números separando-os com vírgula: \n').split(',')

# Converte para integer
for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

# Remove os duplicados
numbers = list(dict.fromkeys(numbers))

# Se os 3 numeros forem iguais, ficara apenas 1 item no array;
if len(numbers) == 1:
    print(f'A potência do número {numbers[0]} elevado a 3 é: {numbers[0] ** 3}')
else:
    print(f'A soma dos números é: {sum(numbers)}')