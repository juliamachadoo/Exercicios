"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
num3 = int(input('Digite um número real: '))

op1 = (num1 * 2) * (num2/2)
op2 = (num1*3) + num3
op3 = num3 ** 3

print(f'o produto do dobro do com metade do segundo = {op1}')
print(f'a soma do triplo do primeiro com o terceiro = {op2}')
print(f'o terceiro valor elevado ao cubo = {op3}')