"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.

"""

print('Vamos calcular a média das notas?')
nota1 = float(input('Qual a nota do 1º Bimestre? '))
nota2 = float(input('Qual a nota do 2º Bimestre? '))
nota3 = float(input('Qual a nota do 3º Bimestre? '))
nota4 = float(input('Qual a nota do 4º Bimestre? '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média das notas {nota1}, {nota2}, {nota3}, {nota4}, é de {media}')
