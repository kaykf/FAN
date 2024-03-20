while True:
    nota = int(input('Digite a primeira nota: '))
    nota2 = int(input('Digite a segunda nota: '))

    if (nota > 10) or (nota2 > 10):
        print('Nota Inválida!')
    elif (nota < 0) or (nota2 < 0):
        print('Nota Inválida!')
    else:
        media = (nota + nota2)/2
        print(media)
        break