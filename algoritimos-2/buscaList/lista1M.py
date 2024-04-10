milhão = [ numero for numero in range(1, 100)]

def buscarBinaria(lista,valor):
    pos_ini = 0
    pos_fim = len(lista)-1

    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim)//2

        if lista[pos_meio] == valor:
            return f'O valor digitado se encontra {pos_meio}'
        if lista[pos_meio] > valor:
            pos_fim = pos_meio - 1
        if lista[pos_meio] < valor:
            pos_ini = pos_meio + 1

    return 'Valor não encontrado'

print(buscarBinaria(milhão, 50))

def buscaSequencial2 (lista, chave):
    n = len(lista)
    for indice in range(n):
        if lista[indice] == chave:
            return f'O valor foi encontrado no indice {indice}'
    return 'não encontrado'

print(buscaSequencial2(milhão, 8))

def buscaSequencial(lista, chave):
    indice = 0
    for numero in lista:
        if numero == chave:
            return f'O valor foi encontrado no indice {indice}'
        indice = indice + 1
    return 'Não encontrado'

print(buscaSequencial(milhão, 100000000))