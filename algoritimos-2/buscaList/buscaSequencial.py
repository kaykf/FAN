listaA = [1,4,6,8,10,5,18,24,28]

def buscaSequencial(lista, chave):
    indice = 0
    for numero in lista:
        if numero == chave:
            return f'O valor foi encontrado no indice {indice}'
        indice = indice + 1
    return 'Não encontrado'

print(buscaSequencial(listaA, 10))

listaB = [1,4,6,8,10,5,18,24,28]

def buscaSequencial2 (lista, chave):
    n = len(lista)
    for indice in range(n):
        if lista[indice] == chave:
            return f'O valor foi encontrado no indice {indice}'
    return 'não encontrado'

print(buscaSequencial2(listaB, 28))