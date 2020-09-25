#Crie uma aplicação Python com uma estrutura
# de classes que atenda aos seguintes requisitos:

# Uma PESSOA precisa realizar um EMPRÉSTIMO de EQUIPAMENTOS de manutenção predial numa companhia especializada.

# Ela pode emprestar uma LISTA DE EQUIPAMENTOS, com data de devolução pré-estabelecida no momento do empréstimo.
import datetime

#Pessoa
class Client:
    def __init__(self, id, name):
        self.id = id
        self.name = name

#Empréstimo
class Lending:
    def __init__(self, id, client, equipements, returnDate):
        self.id = id
        self.client = client
        self.equipements = equipements
        self.returnDate = returnDate

    @property
    def show(self):
        return print('Questão 7 - Empresta aí')

#Equipamento
class Equipment:
    def __init__(self, id, description):
        self.id = id
        self.description = description

equipment_one = Equipment(1, 'Capacete')
equipment_two = Equipment(2, 'Parafuso')
equipment_three = Equipment(3, 'Martelo')
equipment_four = Equipment(4, 'Furadeira')

client_one = Client(1, 'Dave king')
client_two = Client(2, 'Matt hensley')

lending = Lending(1, client_one, [equipment_two, equipment_four], datetime.datetime(2020, 10, 20))

print(f'O empréstimo com o código {lending.id} está relacionado ao cliente {lending.client.name} '
      f' \n emprestou: {lending.equipements[0].description} e {lending.equipements[1].description} a previsão de devolução: {lending.returnDate} ')
