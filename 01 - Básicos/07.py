"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

lado = float(input('Digite o tamanho dos lados do quadrado (em cm): '))

area = lado ** 2
dobro_area = area * 2

print(f'O quadrado de lado {lado}, possui área de {area}cm². E o dobro da sua área é de {dobro_area}cm²')