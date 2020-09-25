#Escreva uma classe Python básica que em seu método inicializador
#receba uma frase informada pelo usuário, e retorne o print da frase em UPPER CASE.
class Basic:
    def __init__(self, desc):
        self.desc = desc
        return print(self.desc.upper())

Basic('Hello Word')