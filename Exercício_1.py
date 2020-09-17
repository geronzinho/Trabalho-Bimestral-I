def prepareList(attempts, attempt):
    list = []
    while(attempt <= attempts):
        print(f'Número {attempt} de {attempts}')
        number = int(input(f'Informando número {attempt} de {attempts} : '))
        list.append(number)
        attempt += 1
    return list

attempts = int(input('Quantos números deseja informar? : '))
attempt = 1
list = prepareList(attempts, attempt)
print(f'PRIMEIRO NÚMERO DA LISTA: {list[0]}')
print(f'ÚLTIMO NÚMERO DA LISTA: {list[-1]}')
print(f'LISTA FINAL: {list}')