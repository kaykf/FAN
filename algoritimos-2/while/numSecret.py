numero_secreto = 42
tentativas = 0

while True:
    tentativa = int(input('Digitar um número: '))
    tentativas += 1
    if tentativa == numero_secreto:
        print('Parabés, você acertou em, ',tentativas, ' tentativas')
        break
    elif tentativa < numero_secreto:
        print('Tente um número maior!')
    else:
        print('Tente um número menor!')