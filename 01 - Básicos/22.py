"""
 Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem:
"""

distancia = float(input('Qual a distancia da viagem? (em quilômetros)'))
velocidade = float(input('Qual a velocidade media esperada para a viagem? '))

tempo = distancia/velocidade

print(f'Para percorrer {distancia}km, numa velocidade de {velocidade}km/h, serão necessarios {tempo} horas para '
      f'completar todo o percurso')