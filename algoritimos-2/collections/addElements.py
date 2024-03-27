par = []
impar = []

for i in range (10):
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(par)
print(impar)

minha_lista = [1,2,3,4,5]

minha_lista.insert(2,8)
print(minha_lista)

minha_lista.append([6,7,8,9])
minha_lista.extend([10,11,12])
print(minha_lista)