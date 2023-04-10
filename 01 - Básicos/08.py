"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

valor_hora = float(input('Qual valor é cobrado por hora de trabalho? '))
quant_horas = int(input('Quantas horas você trabalha por mês?'))

salario = valor_hora * quant_horas

print(f'Recebendo R${valor_hora} por hora e trabalhando {quant_horas} horas por mês, você recebe R${salario} por mês')