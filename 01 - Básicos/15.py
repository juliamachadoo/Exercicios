"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
import math

print('------ BEM VINDO A LOJA DE TINTAS ---------')

largura = float(input('Qual a largura da sua parede(em metros)? '))
comprimento = float(input('Qual o comprimento da sua parede(em metros)? '))

tamanho_parede = largura * comprimento

qnt_litros = (tamanho_parede/3)

qnt_latas = qnt_litros/18

preco_final = qnt_latas * 80

print(f'Para pintar uma parede de {tamanho_parede}m², você gastará {qnt_litros:.2f}L.\nNossa lata possui 18L, '
      f'ou seja, '
      f'você precisará de {math.ceil(qnt_latas)} lata(s).\nO valor a se pagar é de R${preco_final:.2f}')



