
print('----------------------------------')
eleitores = int(input('digite o número de eleitores: '))
print('----------------------------------')

candidato1 = 0
candidato2 = 0
candidato3 = 0

while (candidato1+candidato2+candidato3) < eleitores:
    voto = int(input('digite o seu voto (1, 2 ou 3): '))

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    else:
        print('Voto Inválido')

print('----------------------------------')
print('Candidato 1, votos: ', candidato1)
print('Candidato 2, votos: ', candidato2)
print('Candidato 3, votos: ', candidato3)
print('----------------------------------')
