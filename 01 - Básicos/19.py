"""Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor do novo salário reajustado de acordo com a tabela abaixo:
Salário atual	Reajuste
Abaixo de R$500,00	15%
de R$500,00 até R$1000,00	10%
Acima de R$1000,00	5%"""

salario_atual = float(input('Qual o seu salario atual? '))

if salario_atual < 500:
    novo_salario = salario_atual*1.15
    print(f'Você recebe R${salario_atual}, seu reajuste será de 15%, seu salario passará a ser de R${novo_salario:.2f}')
elif 500 <= salario_atual <= 1000:
    novo_salario = salario_atual*1.1
    print(f'Você recebe R${salario_atual}, seu reajuste será de 10%, seu salario passará a ser de R${novo_salario:.2f}')
else:
    novo_salario = salario_atual*1.05
    print(f'Você recebe R${salario_atual}, seu reajuste será de 5%, seu salario passará a ser de R${novo_salario:.2f}')
