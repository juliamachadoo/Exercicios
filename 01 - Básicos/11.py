"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
altura = float(input('Digite sua altura em metros: '))

peso_ideal = (72.7*altura) - 58

print(f'Para uma pessoa com a altura de {altura}, o peso ideal é de {peso_ideal}')