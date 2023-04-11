class Aluno(object):
    status = False
    n1 = 0
    n2 = 0

    def __init__(self, nome: str):
        self.nome = nome

    def calcular_medias(self):
        media = (self.n1 + self.n2)/2
        return media

    def inserir_nota(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def mostrar_infos(self):
        if self.calcular_medias() >= 6:
            status = True
            print(f'Nome do Aluno: {self.nome}\n'
                  f'Status: {status}')
            print(f'Sua média foi de {self.calcular_medias()}, você está APROVADO')

        else:
            status = False
            print(f'Nome do Aluno: {self.nome}\n'
                  f'Status: {status}')
            print(f'Sua média foi de {self.calcular_medias()}, você está REPROVADO')
aluno = Aluno('Julia')
aluno.inserir_nota(5,8)
aluno.mostrar_infos()