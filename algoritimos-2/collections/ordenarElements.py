listaA = [1,5,3,22,10,45,100,68,12,6,2,3,4,58,235,141,66]

listaA.sort()
print(listaA)

listaName = ['Kayk','João','Pedro','Paulo','André']
listaName.sort()
print(listaName)

listaName.reverse()
listaA.reverse()
print(listaA)
print(listaName)

print(len(listaA))
print(len(listaName))

print(listaA.count(3))

if 5 in listaA:
    print('5 está na lista')
else:
    print('Não existe esse elemento nessa lista')