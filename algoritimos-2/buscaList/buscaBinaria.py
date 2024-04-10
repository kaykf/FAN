listaA = [1,5,15,20,24,45,67,76,78,100]

def buscarBinaria(lista,valor):
    pos_ini = 0
    pos_fim = len(lista)-1

    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim)//2

        if lista[pos_meio] == valor:
            return pos_meio
        if lista[pos_meio] > valor:
            pos_fim = pos_meio - 1
        if lista[pos_meio] < valor:
            pos_ini = pos_meio + 1

    return 'Valor não encontrado'

print(buscarBinaria(listaA, 15))