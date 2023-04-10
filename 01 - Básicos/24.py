class Carro(object):
    def __init__(self, modelo, ano, estado):
        self.modelo = modelo
        self.ano = ano
        self.estado = estado

    def liga_desliga(self):
        pass

    def acelerar(self):
        pass

    def test_drive(self):
        print('O carro é ótimo! Adorei fazer um test drive nele')

    def comprar(self):
        pass

fusca = Carro('Fusca', 1973, 'usado')
bmw = Carro('BMW', 2010, 'novo')
ferrari = Carro('Ferrari', 2022, 'novo')
fusca.test_drive()

class Carro2(object):
    def __init__(self,nome, estado):
        self.nome = nome
        self.estado = estado

    def infos(self):
        print(f'O carro {self.nome} tem o estado {self.estado}')

fusca = Carro('Fusca', 1973, 'usado')
