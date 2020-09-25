#Crie um programa em Python que sirva como calculadora através dos inputs do usuário.
# A calculadora precisará solicitar ao usuário o primeiro número,
# a operação (soma, subtração, multiplicação, divisão, resto divisão), e na sequência solicitar o segundo número.
# Por fim, o programa deverá printar a operação matemática realizada e o resultado.
number_1 = int(input('Primeiro número: '))
operation = input('''
    Insira uma operação para continuar
    + para soma
    - para subtração
    * para multiplicação
    / para divisão
    / para resto de divisão
    ''')
number_2 = int(input('Insira o segundo número:'))


# Soma
if operation == '+':
    print(f'Soma: {number_1} + {number_2} =  {number_1 + number_2}')

# Subtração
elif operation == '-':
    print(f'Subtração: {number_1} - {number_2} = {number_1 - number_2}')

# Multiplicação
elif operation == '*':
    print(f'Multiplicação: {number_1} * {number_2} = {number_1 * number_2}')


# Divisão

elif operation == '/':
    print(f'Divisão: {number_1} / {number_2} = {number_1 / number_2}')

# Resto
elif operation == '%':
    print(f'Resto de divisão: {number_1} % {number_2} = {number_1 % number_2}')

else:
    print('Selecione uma operação válida')
