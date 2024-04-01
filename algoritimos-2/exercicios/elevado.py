def elevar ():
    x = int(input('Digite o valor de X: '))
    z = int(input('Digite o valor de Z: '))
    xz = x**z
    return f'{x} elevado a {z} é igual á {xz}'
print(elevar())