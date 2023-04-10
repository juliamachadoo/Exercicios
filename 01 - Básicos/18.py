"""
Construa um jogo de adivinhação de números, no qual o usuário seleciona um intervalo.
Digamos que o usuário tenha selecionado um intervalo, ou seja, de A a B , onde A e B pertencem a inteiro.
Algum inteiro aleatório será selecionado pelo sistema e o usuário deve adivinhar esse inteiro no número mínimo de adivinhações

"""
import random
from time import sleep

print('--- JOGO DA ADIVINHAÇÃO ---')
sleep(1)
print('Boa tarde Jogador, vamos brincar de adivinha?')
sleep(1)
print('Escolha um intervalo de valores')
n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))

if n2 < n1:
    print('O segundo valor tem que ser maior que o primeiro')
else:
    escolha_computador = random.randint(n1, n2)
    sleep(1)
    print('Já escolhi um número, sera que voce consegue adivinhar?')
    sleep(1)
    escolha_jogador = int(input(f'Qual número entre {n1} e {n2} você acha que eu escolhi?'))

    if escolha_jogador == escolha_computador:
        print('PARABENS! Você leu minha mente?')
    else:
        print(f'Você não acertou :( O número que eu escolhi foi o {escolha_computador}')

