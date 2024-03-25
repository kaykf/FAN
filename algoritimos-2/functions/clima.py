def clima(temperatura):

    if temperatura < 15:
        return ('Está Frio')
    elif (temperatura >= 15) and (temperatura < 28):
        return ('O clima está normal')
    else:
        return('Está quente DEMAIS!')
    
temperatura = int(input('Digite a Temperatura: '))

print(clima(temperatura))