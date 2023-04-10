"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
import math

raio_circulo = float(input('Qual o raio do círculo?'))

area_circulo = math.pi * (raio_circulo**2)

print(f'A área do cículo é de: {area_circulo:.2f}')
