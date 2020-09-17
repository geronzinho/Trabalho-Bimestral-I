def prepareList(attempts, attempt):
    list = []
    while(attempt <= attempts):
        print()
        number = int(input(f'Informando número {attempt} de {attempts} : '))
        list.append(number)
        attempt += 1
    return list

attempts = int(input('Deseja informar quantos números? : '))
attempt = 1
list = prepareList(attempts, attempt)

for number in list:
    print(f'O número elevado ao quadrado ² {number} é {number ** 2}')