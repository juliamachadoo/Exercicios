class Calculadora(object):

    def somar(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        return self.n1 + self.n2

    def subtrair(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        return self.n1 - self.n2

    def multiplicar(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        return self.n1 * self.n2

    def dividir(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        return self.n1/self.n2


calc = Calculadora()

print(calc.somar(5, 10))

print(calc.subtrair(10, 20))