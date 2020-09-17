elements_one = ['Douglas', 'Anderson', 'Libório', 'Maicon', 'Prefeito Géri']
elements_two = ['Douglas', 'Maicon', 'Libório']

result = (list(list(set(elements_one)-set(elements_two)) + list(set(elements_two)-set(elements_one))))

print(result)