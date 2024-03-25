nota1 = int(input('Digite nota 1: '))
nota2 = int(input('Digite nota 2: '))
nota3 = int(input('Digite nota 3: '))
nota4 = int(input('Digite nota 4: '))

def aluno():
    media = (nota1 + nota2 + nota3 + nota4)/4

    if media >= 7:
        return(f'O aluno foi aprovado com a média: {media}')
    else:
        return(f'O aluno foi reprovado com a média: {media}')
    
print(aluno())