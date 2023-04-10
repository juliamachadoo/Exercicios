"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

temp = int(input('Digite uma temperatura(em Fahrenheit): '))
temp_celcius = 5 * ((temp-32) / 9)

temp2 = int(input('Digite uma temperatura(em Celcius): '))
temp_fahr = (temp2 * 1.8) + 32

print(f'A temperatura {temp}ºF equivale a {temp_celcius:.2f}ºC')
print(f'A temperatura {temp2}ºC equivale a {temp_fahr}ºF')
