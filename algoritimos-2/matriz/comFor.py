matriz = [[1,2,3],[4,5,6],[7,8,9]]

for lista in matriz:
    for num in lista:
        print(num)

[[print(valor)for valor in lista] for lista in matriz]