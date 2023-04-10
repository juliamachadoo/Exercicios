"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
tam_arquivo = int(input('Qual o tamanho do arquivo? (em MB)'))
vel_internet = int(input('Qual a velocidade da internet? (em Mbps)'))

tempo_download = tam_arquivo/(vel_internet*60)


print(f'Para fazer o download de um arquivo de {tam_arquivo}MB com a internet a {vel_internet}Mbps, serão necessarios {tempo_download:.2f} minutos')