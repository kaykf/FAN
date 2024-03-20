senha_correta = 'senha123'

tentativa = 0

while tentativa <= 3:
    senha = input('Digite a senha:')

    if senha != senha_correta:
        print('Senha Incorreta, você tem mais, ', (2 - tentativa), " tentativas." )
        tentativa += 1

        if tentativa == 3:
            print('Acesso negado , crie uma nova senha.')
            senha_correta = str(input('Crie uma nova senha: '))
            print('Senha cadastrada com suceso.')
    
    else:
        print('Acesso Liberado')
        break