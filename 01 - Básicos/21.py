"""
Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar:
"""

preco = float(input('Qual o valor da mercadoria? '))
desconto = float(input('Qual o percentual de desconto? '))

valor_desconto= preco * (desconto/100)

novo_preco = preco - valor_desconto

print(f'Comprando a mercadoria de R${preco} e com desconto de {desconto}%, você terá R${valor_desconto} de desconto')
print(f'O novo valor da mercadoria é de R${novo_preco}')