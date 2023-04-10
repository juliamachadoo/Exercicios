"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
import math

print('------ BEM VINDO A LOJA DE TINTAS ---------')

largura = float(input('Qual a largura da sua parede(em metros)? '))
comprimento = float(input('Qual o comprimento da sua parede(em metros)? '))

tamanho_parede = (largura * comprimento) * 1.1

qnt_litros = (tamanho_parede/6)

qnt_latas = math.ceil(qnt_litros/18)
qnt_galoes = math.ceil(qnt_litros/3.6)

preco_final_lata = qnt_latas * 80
preco_final_galao= qnt_galoes * 25

print(f'Para pintar uma parede de {tamanho_parede:.2f}m², você gastará {qnt_litros:.2f}L.\nComprando nossa lata de '
      f'18L, '
      f'você precisará de {math.ceil(qnt_latas)} lata(s).\nO valor a se pagar é de R${preco_final_lata:.2f}.\nCaso '
      f'opte '
      f'por comprar galão, você gastará {math.ceil(qnt_galoes)} galões.\nO valor a se pagar é de R$'
      f'{preco_final_galao:.2f}.')

