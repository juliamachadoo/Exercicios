def media ():
    nota1 = float(input('Qual a nota 1? '))
    nota2 = float(input('Qual a nota 2? '))
    return calcular_media(nota1, nota2)

def calcular_media(nota1, nota2):
    media = (nota1 + nota2)/2
    return media

def calcular_aprovacao(media):
    if media >= 7:
        print(f'Sua média é de {media}. Você esta APROVADO!')
    else:
        print(f'Sua média foi de {media}, você ficou abaixo dela e, por isso, esta REPROVADO.')


calcular_aprovacao(media())