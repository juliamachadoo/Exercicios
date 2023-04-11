class Carro(object):
    comprado = False
    def __init__(self, modelo, ano, estado):
        self.modelo = modelo
        self.ano = ano
        self.estado = estado

    def liga_desliga(self, status):
        if status:
            print('Você ligou o carro')
        else:
            print('Carro desligado')

    def acelerar(self):
        return self.comprado

    def test_drive(self):
        if not self.comprado:
            print('Você ainda não usou esse carro? Vamos fazer o test drive')
            self.liga_desliga(True)
            print('O carro está ligado, vamos fazer o test drive')
            if (self.acelerar()):
                print('Você pode acelerar')
            else:
                print('Você não pode acelerar')
            self.liga_desliga(False)
            print('O carro está desligado. Você terminou de fazer o test-drive')
        else:
            print('Você já possui o carro, não pode fazer o test-drive')

    def comprar(self):
        if(self.comprado):
            print('Você já comprou, não pode comprar novamente')
            return
        else:
            self.comprado = True
            print('PARABÉNS! Você comprou o carro')

    def dirigir(self):
        if self.comprado:
            print('Você vai dirigir!')
            self.liga_desliga(True)
            print('O carro está ligado')
            if (self.acelerar()):
                print('Você pode acelerar')
            else:
                print('Você não pode acelerar')
            self.liga_desliga(False)
            print('O carro está desligado, você não pode mais dirigir')
        else:
            print('Você só pode dirigir se comprar o carro')


ferrari = Carro('Ferrari', 2022, 'Novo')
bmw = Carro(ano=2021, modelo='BMW', estado='Usado')

ferrari.comprar()
ferrari.dirigir()
