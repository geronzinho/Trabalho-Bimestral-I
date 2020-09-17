
def easter(year):
    b = year / 100
    c = (year - 100) * b
    quotient = (5 * b + c) / 19
    a = 5 * b + c - 19 * quotient
    d = (3 * (b + 25)) / 4
    e = 3 * (b + 25) - 4 * d
    g = (8 * (b + 11)) / 25
    quotient = (19 * a + d - g) / 30
    h = 19 * a + d - g - 30 * quotient
    m = (a + 11 * h) / 319
    j = (60 * (5 - e) + c) / 4
    k = 60 * (5 - e) + c - 4 * j
    quotient = (2 * j - k - h + m) / 7
    l = 2 * j - k - h + m - 7 * quotient
    number_month = (h - m + l + 110) / 30 # number_month é o mês (valor numérico)
    q = h - m + l + 110 - 30 * number_month
    quotient = (q + 5 - number_month) / 32
    day = q + 5 - number_month   # p é o dia
    if number_month == 3:
        name_month = 'Março'  # N é o nome do mês
    else:
        name_month = 'Abril'
    if quotient != 0:
        print('Ops! Algo de errado aconteceu')
    else:
        print(f'Em {year} o Domingo de Páscoa é no dia {day} de {name_month}')

easter(2019)