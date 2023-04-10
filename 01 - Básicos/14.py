"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
- salário bruto, quanto pagou ao INSS, quanto pagou ao sindicato, o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

valor_hora = float(input('Qual valor é cobrado por hora de trabalho? '))
quant_horas = int(input('Quantas horas você trabalha por mês?'))

salario_bruto = valor_hora * quant_horas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

descontos = ir + inss + sindicato

salario_liquido = salario_bruto - descontos

print(f'Salário Bruto: R${salario_bruto}\n'
      f'IR (11%): R${ir}\n'
      f'INSS (8%): R${inss}\n'
      f'Sindicato (5%): R${sindicato}\n'
      f'Salário Liquido: R${salario_liquido}')
