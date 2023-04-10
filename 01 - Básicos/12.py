"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.
"""

opcao = int(input('Você é:\n[1] Homem\n[2] Mulher\n'))
altura = float(input('Digite sua altura em metros: '))

if opcao == 1:
    peso_ideal = (72.7*altura) - 58
    print(f'O peso ideal para uma pessoa com altura de {altura} é de {peso_ideal:.2f}')
else:
    peso_ideal = (62.1*altura) - 44.
    print(f'O peso ideal para uma pessoa com altura de {altura} é de {peso_ideal:.2f}')

